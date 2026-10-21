from collections.abc import Callable
from dataclasses import dataclass
from plone import api
from portalbrasil.legislativo.testing import ACCEPTANCE_TESTING
from portalbrasil.legislativo.testing import FUNCTIONAL_TESTING
from portalbrasil.legislativo.testing import INTEGRATION_TESTING
from Products.CMFPlone.Portal import PloneSite
from pytest_plone import fixtures_factory
from typing import Any

import pytest


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory((
        (ACCEPTANCE_TESTING, "acceptance"),
        (FUNCTIONAL_TESTING, "functional"),
        (INTEGRATION_TESTING, "integration"),
    ))
)


@dataclass
class CurrentVersions:
    """Versions of the package and of its GenericSetup profiles."""

    base: str
    default: str
    package: str


@pytest.fixture(scope="session")
def current_versions() -> CurrentVersions:
    """Return the package, base and default profile versions under test."""
    from portalbrasil.legislativo import __version__

    return CurrentVersions(
        base="20261004001",
        default="1000",
        package=__version__,
    )


@pytest.fixture(scope="session")
def distribution_name() -> str:
    """Return the name of the distribution used to create test sites."""
    from portalbrasil.legislativo import DISTRIBUTION_NAME

    return DISTRIBUTION_NAME


@pytest.fixture(scope="session")
def prepare_answers() -> Callable[[], dict[str, Any]]:
    """Return a helper that builds the default site-creation answers."""

    def func() -> dict[str, Any]:
        """Build a fresh copy of the default site-creation answers."""
        return {
            "site_id": "portal",
            "title": "Câmara Modelo",
            "description": "Site da câmara modelo",
            "available_languages": ["pt-br"],
            "default_language": "pt-br",
            "portal_timezone": "America/Sao_Paulo",
            "setup_content": True,
        }

    return func


@pytest.fixture(scope="session")
def answers(prepare_answers: Callable[[], dict[str, Any]]) -> dict[str, Any]:
    """Return the default site-creation answers."""
    return prepare_answers()


@pytest.fixture(scope="session")
def create_site(
    distribution_name: str, site_owner_name: str
) -> Callable[..., PloneSite]:
    """Return a helper that creates (replacing any existing) a Plone site."""
    from plone.distribution.api import site as site_api
    from zope.component.hooks import setSite

    def func(app: Any, answers: dict[str, Any]) -> PloneSite:
        """Create a site from ``answers``, deleting a homonymous one first."""
        with api.env.adopt_user(site_owner_name):
            site_id = answers.get("site_id")
            if site_id and (site_id in app.objectIds()):
                app.manage_delObjects(site_id)
            site = site_api._create_site(
                app, distribution_name=distribution_name, answers=answers
            )
            setSite(site)
        return site

    return func
