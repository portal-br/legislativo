from plone import api
from plone.distribution.api import distribution as dist_api
from plone.distribution.core import Distribution
from portalbrasil.legislativo import _types as t
from portalbrasil.legislativo.utils.packages import package_version


def current_distribution() -> Distribution:
    """Return the distribution for the current portal."""
    portal = api.portal.get()
    report = dist_api.get_creation_report(portal)
    if not report:
        raise ValueError("No distribution report found for the current portal.")
    distribution = dist_api.get(report.name)
    return distribution


def distribution_info() -> t.DistributionInfo:
    """Return distribution information for the current site."""
    distribution = current_distribution()
    version = package_version(distribution.package)
    return {
        "name": distribution.name,
        "title": distribution.title,
        "package_name": distribution.package,
        "package_version": version,
    }
