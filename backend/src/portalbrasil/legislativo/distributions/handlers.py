from plone.distribution.core import Distribution
from plone.distribution.utils.data import convert_data_uri_to_b64
from portalbrasil.legislativo import logger
from portalbrasil.legislativo.utils import creation as utils
from Products.CMFPlone.Portal import PloneSite
from typing import Any

import transaction


def pre_handler(answers: dict[str, Any]) -> dict[str, Any]:
    """Process answers.

    Handle cases where available_languages is not provided but default_language is, or
    where default_language is not in available_languages.
    This ensures that the site will always have a valid default language and that
    the available languages are consistent with the default language.

    :param answers: Answers provided for the site creation.
    :returns: The processed answers.
    """
    available_languages = answers.get("available_languages")
    default_language = answers.get("default_language")
    if available_languages is None and default_language:
        answers["available_languages"] = [default_language]
    elif available_languages and default_language not in available_languages:
        answers["default_language"] = available_languages[0]
    return answers


def handler(
    distribution: Distribution, site: PloneSite, answers: dict[str, Any]
) -> PloneSite:
    """Handler to create a new site.

    :param distribution: Distribution used to create the site.
    :param site: The new Plone site.
    :param answers: Answers provided for the site creation.
    :returns: The Plone site.
    """
    tx = transaction.get()
    # If there is no savepoint most tests fail with a PosKeyError
    tx.savepoint(optimistic=True)
    # Add example content if needed
    if answers.get("setup_content", False):
        utils.create_example_content(site, distribution, tx)
    tx.savepoint(optimistic=True)

    # Commit the transaction to finalize the import
    tx.description = f"Created site {site.id} with distribution {distribution.name}"
    tx.commit()
    return site


def post_handler(
    distribution: Distribution, site: PloneSite, answers: dict[str, Any]
) -> PloneSite:
    """Run after site creation.

    :param distribution: Distribution used to create the site.
    :param site: The new Plone site.
    :param answers: Answers provided for the site creation.
    :returns: The Plone site.
    """
    name = distribution.name
    logger.info(f"{site.id}: Running {name} post_handler")
    # This should be fixed on plone.distribution
    title = answers.get("title", site.title)
    description = answers.get("description", site.description)
    raw_logo = answers.get("site_logo")
    registry_data: dict[str, Any] = {
        "plone.email_from_name": title,
        "plone.site_title": title,
    }
    if raw_logo:
        logo = convert_data_uri_to_b64(raw_logo)
        registry_data["plone.site_logo"] = logo

    # Update site content
    utils.update_content(site, title, description, raw_logo)
    # Update registry
    utils.update_registry(registry_data)
    # Update permissions
    utils.update_permissions()
    return site
