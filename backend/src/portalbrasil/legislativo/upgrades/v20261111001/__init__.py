"""Upgrade to 20261111001: Plone 6.2.3, Volto 19.7.0 and sc.voltolighttheme 1.0.0a15."""

from portalbrasil.legislativo import logger
from Products.GenericSetup.tool import SetupTool


#: Add-on profiles whose packages changed in this release and that the site
#: installs, in dependency order. ``plone.restapi`` and ``plone.volto`` come
#: first, as in the ``portal_migration`` list. ``plonetheme.barceloneta`` is
#: not listed: it changed only in its package, and the site does not use it.
#: ``kitconcept.voltolighttheme`` is not listed on purpose: the
#: ``sc.voltolighttheme`` 1000 to 1001 step uninstalls it.
DEPENDENCIES = (
    "plone.restapi:default",
    "plone.volto:default",
    "sc.voltolighttheme:default",
)


def upgrade_dependencies(setup_tool: SetupTool) -> None:
    """Run the pending upgrade steps of the add-ons updated in this release.

    Only the pending steps of each profile run. The Plone core migration
    (``portal_migration``) is not run from here.

    :param setup_tool: The ``portal_setup`` tool.
    """
    for profile_id in DEPENDENCIES:
        before = setup_tool.getLastVersionForProfile(profile_id)
        setup_tool.upgradeProfile(profile_id)
        after = setup_tool.getLastVersionForProfile(profile_id)
        logger.info("Upgraded %s from %s to %s", profile_id, before, after)
