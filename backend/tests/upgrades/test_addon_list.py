from . import NOT_UPGRADED_PROFILES
from . import PROFILES_WITH_PENDING_UPGRADES
from . import UPGRADED_PROFILES
from portalbrasil.legislativo import PACKAGE_NAME
from portalbrasil.legislativo.factory import LocalAddonList
from portalbrasil.legislativo.tools.migration import MigrationTool
from Products.CMFPlone.MigrationTool import AddonList
from Products.GenericSetup.tool import SetupTool

import pytest


THEME_PROFILE = "sc.voltolighttheme:default"


class TestAddonList:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the migration tool to the test instance."""
        self.tool: MigrationTool = portal.portal_migration

    @property
    def profile_ids(self) -> list[str]:
        """Return the profile ids of the add-on list used by the tool."""
        return [addon.profile_id for addon in self.tool.get_addon_list()]

    def test_utility(self):
        """The migration tool uses the add-on list of this package."""
        assert self.tool.get_package_name() == PACKAGE_NAME
        assert self.tool.get_addon_list() is LocalAddonList.addon_list

    def test_pre_addon_list(self):
        """No add-on is upgraded before the main migration."""
        pre_addon_list = self.tool.get_pre_addon_list()
        assert isinstance(pre_addon_list, AddonList)
        assert list(pre_addon_list) == []

    @pytest.mark.parametrize("profile_id", UPGRADED_PROFILES)
    def test_upgraded(self, profile_id: str):
        """The add-on is upgraded with the site."""
        assert profile_id in self.profile_ids

    @pytest.mark.parametrize("profile_id", NOT_UPGRADED_PROFILES)
    def test_not_upgraded(self, profile_id: str):
        """The add-on is not upgraded with the site."""
        assert profile_id not in self.profile_ids

    def test_order(self):
        """Dependencies are upgraded before the Portal Modelo profile."""
        ids = self.profile_ids
        positions = [ids.index(profile_id) for profile_id in UPGRADED_PROFILES]
        assert positions == sorted(positions)
        assert ids[-1] == f"{PACKAGE_NAME}:default"

    @pytest.mark.parametrize("profile_id", UPGRADED_PROFILES)
    def test_safe(self, profile_id: str):
        """Every add-on in the list can be imported."""
        addon = next(
            addon
            for addon in self.tool.get_addon_list()
            if addon.profile_id == profile_id
        )
        assert addon.safe() is True


class TestUpgrade:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the migration and setup tools to the test instance."""
        self.tool: MigrationTool = portal.portal_migration
        self.setup_tool: SetupTool = portal.portal_setup

    def test_upgrades_theme(self):
        """Upgrading the site runs the pending steps of the theme."""
        last = self.setup_tool.getLastVersionForProfile(THEME_PROFILE)
        self.setup_tool.setLastVersionForProfile(THEME_PROFILE, "1000")
        assert self.setup_tool.listUpgrades(THEME_PROFILE) != []
        self.tool.upgrade()
        assert self.setup_tool.getLastVersionForProfile(THEME_PROFILE) == last
        assert self.setup_tool.listUpgrades(THEME_PROFILE) == []

    @pytest.mark.parametrize(
        "profile_id",
        [
            profile_id
            for profile_id in UPGRADED_PROFILES
            if profile_id not in PROFILES_WITH_PENDING_UPGRADES
        ],
    )
    def test_no_pending_upgrades(self, profile_id: str):
        """A new site has no pending upgrade for the add-on."""
        assert self.setup_tool.listUpgrades(profile_id) == []

    @pytest.mark.parametrize("profile_id", PROFILES_WITH_PENDING_UPGRADES)
    def test_upgrade_clears_pending(self, profile_id: str):
        """Upgrading the site runs the steps a new site starts with."""
        assert self.setup_tool.listUpgrades(profile_id) != []
        self.tool.upgrade()
        assert self.setup_tool.listUpgrades(profile_id) == []
