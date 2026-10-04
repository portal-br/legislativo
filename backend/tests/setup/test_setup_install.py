from . import INSTALLED_PROFILES
from . import UNINSTALLED_PROFILES
from portalbrasil.legislativo import PACKAGE_NAME
from Products.GenericSetup.tool import SetupTool

import pytest


class TestSetupInstall:
    @pytest.fixture(autouse=True)
    def _setup(self, portal, current_versions) -> None:
        """Bind the site and the profile versions to the test instance."""
        self.portal = portal
        self.profile_version: str = current_versions.base
        self.default_profile_version: str = current_versions.default

    def test_browserlayer(self, browser_layers):
        """Test that IBrowserLayer is registered."""
        from portalbrasil.legislativo.interfaces import IBrowserLayer

        assert IBrowserLayer in browser_layers

    def test_latest_version(self, profile_last_version):
        """Test latest version of the base profile."""
        assert profile_last_version(f"{PACKAGE_NAME}:base") == self.profile_version

    def test_base_profile(self, setup_tool):
        """Test if we have the base profile."""
        assert setup_tool.getBaselineContextID() == f"profile-{PACKAGE_NAME}:base"

    def test_default_profile_version(self, profile_last_version):
        """Test latest version of the default profile."""
        assert (
            profile_last_version(f"{PACKAGE_NAME}:default")
            == self.default_profile_version
        )


class TestSetupDependencies:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the site setup tool to the test instance."""
        self.setup_tool: SetupTool = portal.portal_setup

    @pytest.mark.parametrize("profile", INSTALLED_PROFILES)
    def test_installed(self, profile: str):
        """Test if a profile is installed."""
        assert self.setup_tool.getLastVersionForProfile(profile) != "unknown"

    @pytest.mark.parametrize("profile", UNINSTALLED_PROFILES)
    def test_uninstalled(self, profile: str):
        """Test if a profile is not installed."""
        assert self.setup_tool.getLastVersionForProfile(profile) == "unknown"
