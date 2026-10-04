from AccessControl.SecurityManagement import newSecurityManager
from collections.abc import Sequence
from OFS.Application import Application
from pathlib import Path
from portalbrasil.legislativo import DISTRIBUTION_NAME
from portalbrasil.legislativo import logger
from portalbrasil.legislativo.factory import add_site
from portalbrasil.legislativo.interfaces import IBrowserLayer
from Products.CMFPlone.Portal import PloneSite
from Products.GenericSetup.tool import SetupTool
from Testing.makerequest import makerequest
from typing import Any
from zope.interface import directlyProvidedBy
from zope.interface import directlyProvides
from zope.interface.interface import InterfaceClass
from ZPublisher.HTTPRequest import HTTPRequest

import json
import logging
import os
import transaction


marker = object()  # Unique marker object to indicate no value
truthy = frozenset(("t", "true", "y", "yes", "on", "1"))


def as_bool(s: Any) -> bool:
    """Coerce a value into a boolean.

    :param s: Value to coerce. ``None`` yields ``False``; an existing ``bool``
        is returned unchanged; any other value is stringified, stripped, and
        compared case-insensitively against :data:`truthy`.
    :returns: ``True`` if ``s`` represents a truthy string, ``False`` otherwise.
    """
    if s is None:
        return False
    if isinstance(s, bool):
        return s
    s = str(s).strip()
    return s.lower() in truthy


def as_list(value: str) -> list[str]:
    """Split a comma-separated string into a list of trimmed values.

    :param value: Comma-separated string, e.g. ``"en, de, fr"``. An empty or
        falsy value yields an empty list.
    :returns: List of whitespace-stripped items.
    """
    if not value:
        return []
    items = value.split(",")
    return [item.strip() for item in items]


OPTIONS: tuple[tuple[str, str, Any], ...] = (
    ("site_id", "SITE_ID", None),
    ("title", "SITE_TITLE", None),
    ("description", "SITE_DESCRIPTION", None),
    ("available_languages", "SITE_AVAILABLE_LANGUAGES", as_list),
    ("default_language", "SITE_DEFAULT_LANGUAGE", None),
    ("portal_timezone", "SITE_PORTAL_TIMEZONE", None),
    ("setup_content", "SITE_SETUP_CONTENT", as_bool),
)


def parse_answers(answers_file: Path, answers_env: dict[str, Any]) -> dict[str, Any]:
    """Load site-creation answers from a JSON file and override them from the
    environment.

    Answers are read from ``answers_file``; for each key present in that file,
    a matching value in ``answers_env`` takes precedence. The ``setup_content``
    key is coerced with :func:`as_bool` when a value is
    supplied. Empty or missing environment values leave the file value
    untouched.

    :param answers_file: Path to a JSON file holding the base answers.
    :param answers_env: Mapping of answer keys to environment-provided
        overrides, typically produced by :func:`get_environmental_variables`.
    :returns: The merged answers mapping.
    """
    answers: dict[str, Any] = json.loads(answers_file.read_text())
    for key in answers:
        env_value = answers_env.get(key, "")
        if key == "setup_content" and env_value.strip():
            env_value = as_bool(env_value)
        elif not env_value:
            continue
        # Override answers_file value
        answers[key] = env_value
    return answers


def _prepare_loggers() -> None:
    """Configure logging output and silence noisy third-party loggers."""
    logging.basicConfig(format="%(message)s")
    logger.setLevel(logging.INFO)
    # Silence some loggers
    for logger_name in [
        "GenericSetup.componentregistry",
        "Products.MimetypesRegistry.MimeTypesRegistry",
    ]:
        logging.getLogger(logger_name).setLevel(logging.ERROR)


def _prepare_request(
    app: Application, package_ifaces: tuple[type[InterfaceClass], ...] = ()
) -> None:
    """Mark the application request with the required browser layers.

    :param app: The Zope application object whose ``REQUEST`` is decorated.
    :param package_ifaces: Additional browser-layer interfaces to provide on
        the request, on top of :class:`IBrowserLayer` and any interfaces the
        request already provides.
    """
    request: HTTPRequest = app.REQUEST
    ifaces: list[type[InterfaceClass]] = [IBrowserLayer]
    if package_ifaces:
        ifaces.extend(list(package_ifaces))
    for iface in directlyProvidedBy(request):
        ifaces.append(iface)

    directlyProvides(request, *ifaces)


def _prepare_user(app: Application) -> None:
    """Authenticate the security context as the ``admin`` user.

    :param app: The Zope application object providing ``acl_users``.
    """
    admin = app.acl_users.getUserById("admin")
    admin = admin.__of__(app.acl_users)
    newSecurityManager(None, admin)


def _install_additional_profiles(
    site: PloneSite, additional_profiles: Sequence[str]
) -> None:
    """Run all import steps for each of the given GenericSetup profiles.

    :param site: The Plone site whose ``portal_setup`` tool applies the
        profiles.
    :param additional_profiles: Profile ids to install. An empty sequence is a
        no-op.
    """
    if not additional_profiles:
        return
    setup_tool: SetupTool = site.portal_setup
    for profile in additional_profiles:
        logger.info(f" - Installing additional profile {profile}")
        setup_tool.runAllImportStepsFromProfile(profile)


def get_environmental_variables(
    options: tuple[tuple[str, str, Any], ...] = OPTIONS,
) -> dict[str, Any]:
    """Collect site-creation answers from environment variables.

    Each entry in :data:`OPTIONS` maps an answer key to an environment variable
    name and an optional transform callable (e.g. :func:`as_bool`,
    :func:`as_list`). Variables that are not set are skipped, so the resulting
    mapping only contains keys explicitly provided via the environment. Keys
    containing a ``.`` (e.g. ``authentication.provider``) are expanded into a
    nested dictionary.

    :param options: Triples of ``(answer key, environment variable name,
        transform)`` to read; defaults to :data:`OPTIONS`.
    :returns: Mapping of answer keys to their (optionally transformed) values,
        ready to be merged into the site-creation answers.
    """
    env_vars: dict[str, Any] = {}
    for key, env_var, transform in options:
        value = os.getenv(env_var, marker)
        if value is marker:
            continue
        elif transform:
            value = transform(value)
        if "." in key:
            # Handle nested keys (e.g. ``group.key``)
            main_key, sub_key = key.split(".", 1)
            if main_key not in env_vars:
                env_vars[main_key] = {}
            env_vars[main_key][sub_key] = value
        else:
            env_vars[key] = value
    return env_vars


def _create_site(
    app: Application,
    delete_existing: bool,
    answers: dict[str, Any],
    package_ifaces: tuple[type[InterfaceClass], ...] = (),
    additional_profiles: Sequence[str] = (),
) -> PloneSite:
    """Create (or reuse) a Plone site inside the Zope application.

    Prepares the request, security context and loggers, then adds a site with
    id ``answers["site_id"]``. The distribution is always
    ``portalmodelo``: it is written into ``answers``, overriding any
    ``distribution`` key already present there. If a site with that id already
    exists it is reused, unless ``delete_existing`` is set, in which case it is
    removed and recreated. Additional GenericSetup profiles are installed on
    newly created sites.

    :param app: The Zope application object.
    :param delete_existing: When ``True``, delete a pre-existing site with the
        same id before creating a new one.
    :param answers: Site-creation parameters passed through to
        :func:`~portalbrasil.legislativo.factory.add_site`; must contain ``site_id``.
    :param package_ifaces: Additional browser-layer interfaces to provide on
        the request.
    :param additional_profiles: GenericSetup profile ids to install on a newly
        created site.
    :returns: The created or reused Plone site.
    """
    _prepare_loggers()
    app = makerequest(app)
    _prepare_request(app, package_ifaces)
    _prepare_user(app)
    distribution = DISTRIBUTION_NAME
    answers["distribution"] = distribution
    site_id = answers["site_id"]

    logger.info(f"Criando um novo Portal Modelo @ {site_id}")
    logger.info(f" - Usando a distribuição {distribution}")

    if site_id in app.objectIds():
        if delete_existing:
            with transaction.manager:
                app.manage_delObjects([site_id])
            logger.info(f" - Deleted existing site with id {site_id}")
        else:
            logger.info(
                " - Stopping site creation, as there is already a site with id "
                f"{site_id} at the instance. Set DELETE_EXISTING=1 to delete "
                "the existing site before creating a new one."
            )

    app._p_jar.sync()
    if site_id not in app.objectIds():
        with transaction.manager:
            site = add_site(app, **answers)
            _install_additional_profiles(site, additional_profiles)
        logger.info(f" - Site {site.id} created!")
    else:
        site = app[site_id]
    return site


def create_site(
    app: Application,
    answers_file: Path,
    env_answers: dict[str, Any],
    package_iface: type[InterfaceClass] | Sequence[type[InterfaceClass]] | None = None,
    additional_profiles: Sequence[str] = (),
) -> PloneSite:
    """Create a new Plone site from a JSON answers file and the environment.

    High-level entry point that resolves configuration from ``answers_file``
    and the environment, then delegates the actual creation to
    :func:`_create_site`. The distribution is always
    :data:`~portalbrasil.legislativo.DISTRIBUTION_NAME` and the field mapping is
    always :data:`OPTIONS`. The ``DELETE_EXISTING`` environment variable
    controls whether a pre-existing site with the same id is removed before
    creation. When ``env_answers`` is empty, overrides are collected via
    :func:`get_environmental_variables`.

    :param app: The Zope application object.
    :param answers_file: Path to the JSON file holding the base answers.
    :param env_answers: Pre-computed environment overrides; when falsy they are
        gathered from the environment using :data:`OPTIONS`.
    :param package_iface: A single browser-layer interface or a sequence of
        them to provide on the request, or ``None``.
    :param additional_profiles: GenericSetup profile ids to install on a newly
        created site.
    :returns: The created or reused Plone site.
    :raises FileNotFoundError: If ``answers_file`` does not exist.
    :raises json.JSONDecodeError: If ``answers_file`` is not valid JSON.
    :raises KeyError: If the resolved answers do not contain ``site_id``.
    """
    package_ifaces: tuple[type[InterfaceClass], ...] = ()
    delete_existing = as_bool(os.getenv("DELETE_EXISTING"))
    if not env_answers:
        # Extract answers from environment variables
        env_answers = get_environmental_variables(OPTIONS)
    if isinstance(package_iface, Sequence):
        package_ifaces = tuple(package_iface)
    elif package_iface:
        package_ifaces = (package_iface,)
    # Load site creation parameters
    answers = parse_answers(answers_file, env_answers)
    return _create_site(
        app=app,
        delete_existing=delete_existing,
        answers=answers,
        package_ifaces=package_ifaces,
        additional_profiles=additional_profiles,
    )
