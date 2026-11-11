"""Upgrade to 20261111001: Plone 6.2.3, Volto 19.7.0 and sc.voltolighttheme 1.0.0a15."""

from portalbrasil.legislativo import logger
from Products.GenericSetup.tool import SetupTool


#: Plone core profile whose steps (``plone.app.upgrade``) reach 6.2.3.
CORE_PROFILE = "Products.CMFPlone:plone"

#: Add-on profiles whose packages changed in this release and that the site
#: installs, in dependency order. ``plone.restapi`` and ``plone.volto`` come
#: first, as in the ``portal_migration`` list. ``plone.app.querystring`` 15 to
#: 16 adds the ``currentUID`` operation and makes ``path`` sortable.
#: ``plonetheme.barceloneta`` is not listed: it changed only in its package,
#: and the site does not use it. ``kitconcept.voltolighttheme`` is not listed
#: on purpose: the ``sc.voltolighttheme`` 1000 to 1001 step uninstalls it.
DEPENDENCIES = (
    "plone.restapi:default",
    "plone.app.querystring:default",
    "plone.volto:default",
    "sc.voltolighttheme:default",
)


def upgrade_core(setup_tool: SetupTool) -> None:
    """Run the pending steps of the Plone core profile, when the site records it.

    Sites created by this distribution never record the version of the core
    profile, which reads ``unknown``. Running its steps from there would replay
    every historic step, so such sites are left alone: their registry already
    has the defaults of the core profile. Sites that do record it get the
    core's own steps, such as the IImagingSchema change of Plone 6.2.2
    (6204 to 6205) and the null step of 6.2.3 (6205 to 6206).

    :param setup_tool: The ``portal_setup`` tool.
    """
    before = setup_tool.getLastVersionForProfile(CORE_PROFILE)
    if before == "unknown":
        logger.info("Kept %s: its version is not recorded on this site", CORE_PROFILE)
        return
    setup_tool.upgradeProfile(CORE_PROFILE)
    after = setup_tool.getLastVersionForProfile(CORE_PROFILE)
    logger.info("Upgraded %s from %s to %s", CORE_PROFILE, before, after)


def upgrade_dependencies(setup_tool: SetupTool) -> None:
    """Run the pending upgrade steps of the add-ons updated in this release.

    Only the pending steps of each profile run. The Plone core migration
    (``portal_migration``) is not run from here; the core profile is handled
    by :func:`upgrade_core`.

    :param setup_tool: The ``portal_setup`` tool.
    """
    for profile_id in DEPENDENCIES:
        before = setup_tool.getLastVersionForProfile(profile_id)
        setup_tool.upgradeProfile(profile_id)
        after = setup_tool.getLastVersionForProfile(profile_id)
        logger.info("Upgraded %s from %s to %s", profile_id, before, after)
