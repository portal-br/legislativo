"""Upgrade to 20261111001: the core profile and the dependency add-ons run their pending steps."""

from plone.registry.interfaces import IRegistry
from portalbrasil.legislativo.tools.migration import MigrationTool
from portalbrasil.legislativo.upgrades.v20261111001 import CORE_PROFILE
from portalbrasil.legislativo.upgrades.v20261111001 import DEPENDENCIES
from Products.GenericSetup.tool import SetupTool
from zope.component import getUtility

import pytest


PROFILE = "portalbrasil.legislativo:base"
SOURCE = "20261004001"
DESTINATION = "20261111001"
#: The run goes on to the next step, the null step of 20261113001.
CURRENT = "20261113001"
QUERYSTRING_PROFILE = "plone.app.querystring:default"
CURRENT_UID_PREFIX = "plone.app.querystring.operation.string.currentUID."
CURRENT_UID_OPERATION = "plone.app.querystring.queryparser._currentUID"

#: A version below the latest one for each dependency, so that it has
#: pending upgrade steps when the site is at ``SOURCE``.
OLDER_VERSIONS = {
    "plone.restapi:default": "0001",
    "plone.app.querystring:default": "15",
    "plone.volto:default": "1010",
    "sc.voltolighttheme:default": "1000",
}


class TestUpgrade:
    """The step from ``20261004001`` to ``20261111001``."""

    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the setup tool and put the site back at the source version."""
        self.setup_tool: SetupTool = portal.portal_setup
        self.setup_tool.setLastVersionForProfile(PROFILE, SOURCE)

    def _steps(self) -> list[dict]:
        """Return the upgrade steps available from the source version.

        ``listUpgrades`` gives the steps of an ``upgradeSteps`` group as one
        list, and a lone ``upgradeStep`` as a bare info.
        """
        steps: list[dict] = []
        for entry in self.setup_tool.listUpgrades(PROFILE):
            steps.extend(entry if isinstance(entry, list) else [entry])
        return steps

    def _run(self) -> None:
        """Upgrade the base profile from the source version, as the site does."""
        self.setup_tool.upgradeProfile(PROFILE)

    def test_available(self):
        """The site at the source version is offered the two handlers of this step.

        ``listUpgrades`` also offers the step that follows, to the current version.
        """
        steps = self._steps()

        assert [(s["ssource"], s["sdest"]) for s in steps] == [
            (SOURCE, DESTINATION),
            (SOURCE, DESTINATION),
            (DESTINATION, CURRENT),
        ]

    @pytest.mark.parametrize("profile_id", DEPENDENCIES)
    def test_runs_pending_steps(self, profile_id: str):
        """Running the step leaves no pending upgrade step in the dependency."""
        self.setup_tool.setLastVersionForProfile(profile_id, OLDER_VERSIONS[profile_id])
        assert self.setup_tool.listUpgrades(profile_id) != []

        self._run()

        assert self.setup_tool.listUpgrades(profile_id) == []

    def test_querystring_currentuid_registered(self):
        """The 15 to 16 step of plone.app.querystring registers the currentUID operation."""
        registry = getUtility(IRegistry)
        for name in [n for n in registry.records if n.startswith(CURRENT_UID_PREFIX)]:
            del registry.records[name]
        self.setup_tool.setLastVersionForProfile(QUERYSTRING_PROFILE, "15")

        self._run()

        assert registry[CURRENT_UID_PREFIX + "operation"] == CURRENT_UID_OPERATION

    def test_core_profile_recorded_runs_its_steps(self):
        """A site that records the core profile gets the 6.2.2 IImagingSchema change."""
        registry = getUtility(IRegistry)
        variants = registry.records["plone.picture_variants"].value
        variants["small"]["sourceset"] = [
            {"scale": "preview", "additionalScales": ["large", "larger"]}
        ]
        registry["plone.picture_variants"] = variants
        self.setup_tool.setLastVersionForProfile(CORE_PROFILE, "6204")

        self._run()

        sourceset = registry.records["plone.picture_variants"].value["small"][
            "sourceset"
        ]
        assert "sizes" in sourceset[0]
        assert self.setup_tool.getLastVersionForProfile(CORE_PROFILE) == ("6206",)

    def test_core_profile_unrecorded_is_kept(self, monkeypatch):
        """A site without a recorded core version never has the core profile upgraded."""
        calls: list[str] = []
        original = SetupTool.upgradeProfile

        def spy(self, profile_id, *args, **kwargs):
            calls.append(profile_id)
            return original(self, profile_id, *args, **kwargs)

        monkeypatch.setattr(SetupTool, "upgradeProfile", spy)
        assert self.setup_tool.getLastVersionForProfile(CORE_PROFILE) == "unknown"

        self._run()

        assert CORE_PROFILE not in calls
        assert self.setup_tool.getLastVersionForProfile(PROFILE) == (CURRENT,)

    def test_does_not_run_migration(self, monkeypatch):
        """The step never calls the migration tool's own upgrade."""

        def forbidden(self, *args, **kwargs):
            raise AssertionError("portal_migration.upgrade must not run")

        monkeypatch.setattr(MigrationTool, "upgrade", forbidden)

        self._run()

        assert self.setup_tool.getLastVersionForProfile(PROFILE) == (CURRENT,)
