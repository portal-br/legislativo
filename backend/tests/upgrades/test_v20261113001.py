"""Upgrade to 20261113001: the null step lets the migration tool run the add-on list."""

from Products.GenericSetup.tool import SetupTool

import pytest


PROFILE = "portalbrasil.legislativo:base"
SOURCE = "20261111001"
DESTINATION = "20261113001"


class TestUpgrade:
    """The step from ``20261111001`` to ``20261113001``."""

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

    def test_available(self):
        """The site at the source version is offered exactly this step."""
        steps = self._steps()

        assert [(s["ssource"], s["sdest"]) for s in steps] == [(SOURCE, DESTINATION)]

    def test_reaches_destination(self):
        """Running the step records the destination version of the base profile."""
        self.setup_tool.upgradeProfile(PROFILE)

        assert self.setup_tool.getLastVersionForProfile(PROFILE) == (DESTINATION,)
        assert self.setup_tool.listUpgrades(PROFILE) == []

    def test_upgrades_no_other_profile(self, monkeypatch):
        """The null step never upgrades another profile itself."""
        calls: list[str] = []
        original = SetupTool.upgradeProfile

        def spy(self, profile_id, *args, **kwargs):
            calls.append(profile_id)
            return original(self, profile_id, *args, **kwargs)

        monkeypatch.setattr(SetupTool, "upgradeProfile", spy)

        self.setup_tool.upgradeProfile(PROFILE)

        assert calls == [PROFILE]
