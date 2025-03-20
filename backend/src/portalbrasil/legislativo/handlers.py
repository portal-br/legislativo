from plone import api
from plone.distribution.core import Distribution
from plone.distribution.handler import default_handler
from portalbrasil.legislativo import logger
from Products.CMFPlone.Portal import PloneSite


def pre_handler(answers: dict) -> dict:
    """Process answers."""
    return answers


def handler(distribution: Distribution, site: PloneSite, answers: dict) -> PloneSite:
    """Handler to create a new site."""
    site = default_handler(distribution, site, answers)
    return site


def post_handler(
    distribution: Distribution, site: PloneSite, answers: dict
) -> PloneSite:
    """Run after site creation."""
    name = distribution.name
    logger.info(f"{site.id}: Running {name} post_handler")
    # This should be fixed on plone.distribution
    site.title = answers.get("title", site.title)
    site.description = answers.get("description", site.description)
    api.portal.set_registry_record("plone.site_title", site.title)
    return site
