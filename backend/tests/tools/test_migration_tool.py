from . import CORE_VERSION_KEYS
from portalbrasil.legislativo import __version__
from portalbrasil.legislativo import PACKAGE_NAME
from portalbrasil.legislativo.tools.migration import MigrationTool
from zope.component.hooks import site

import pytest


class TestMigrationTool:
    @pytest.fixture(autouse=True)
    def _setup(self, portal, current_versions) -> None:
        """Bind the migration tool and the base profile version to the test."""
        self.tool: MigrationTool = portal.portal_migration
        self.profile_version = current_versions.base

    def test_is_instance(self):
        """portal_migration uses our class."""
        assert isinstance(self.tool, MigrationTool)

    def test_getSoftwareVersion(self):
        """The software version is the package version."""
        assert self.tool.getSoftwareVersion() == __version__

    def test_getFileSystemVersion(self):
        """The file system version is the base profile version."""
        assert self.tool.getFileSystemVersion() == self.profile_version

    def test_getInstanceVersion(self):
        """The instance version is the base profile version."""
        assert self.tool.getInstanceVersion() == self.profile_version

    def test_list_steps(self):
        """There are no pending upgrade steps."""
        assert self.tool.list_steps() == []

    def test_coreVersions_core(self):
        """The core entry describes this package."""
        assert self.tool.coreVersions()["core"] == {
            "name": PACKAGE_NAME,
            "package_version": __version__,
            "instance_version": self.profile_version,
            "fs_version": self.profile_version,
        }

    @pytest.mark.parametrize("key,expected", [("Zope", "6.2"), ("CMFPlone", "6.2.2")])
    def test_coreVersions_values(self, key: str, expected: str):
        """Versions match the pinned stack."""
        assert self.tool.coreVersions()[key] == expected

    @pytest.mark.parametrize("key", CORE_VERSION_KEYS)
    def test_coreVersions_keys(self, key: str):
        """coreVersions exposes the expected keys."""
        assert key in self.tool.coreVersions()

    @pytest.mark.parametrize("key", CORE_VERSION_KEYS)
    def test_coreVersions_keys_without_site_hook(self, key: str):
        """coreVersions works without the site hook being set."""
        with site(None):
            info = self.tool.coreVersions()
        assert key in info
