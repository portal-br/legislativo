"""Upgrade to 20261111001: the theme and dependency add-ons run their pending steps."""

from portalbrasil.legislativo.tools.migration import MigrationTool
from portalbrasil.legislativo.upgrades.v20261111001 import DEPENDENCIES
from Products.GenericSetup.tool import SetupTool

import pytest


PROFILE = "portalbrasil.legislativo:base"
SOURCE = "20261004001"
DESTINATION = "20261111001"

#: A version below the latest one for each dependency, so that it has
#: pending upgrade steps when the site is at ``SOURCE``.
OLDER_VERSIONS = {
    "plone.restapi:default": "0001",
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
        """The site at the source version is offered exactly this step."""
        steps = self._steps()

        assert [(s["ssource"], s["sdest"]) for s in steps] == [(SOURCE, DESTINATION)]

    @pytest.mark.parametrize("profile_id", DEPENDENCIES)
    def test_runs_pending_steps(self, profile_id: str):
        """Running the step leaves no pending upgrade step in the dependency."""
        self.setup_tool.setLastVersionForProfile(profile_id, OLDER_VERSIONS[profile_id])
        assert self.setup_tool.listUpgrades(profile_id) != []

        self._run()

        assert self.setup_tool.listUpgrades(profile_id) == []

    def test_does_not_run_migration(self, monkeypatch):
        """The step never calls the Plone core migration."""

        def forbidden(self, *args, **kwargs):
            raise AssertionError("portal_migration.upgrade must not run")

        monkeypatch.setattr(MigrationTool, "upgrade", forbidden)

        self._run()

        assert self.setup_tool.getLastVersionForProfile(PROFILE) == (DESTINATION,)
