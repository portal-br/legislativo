from portalbrasil.core.tools.migration import MigrationTool

import pytest


class TestMigrationTool:
    @pytest.fixture(autouse=True)
    def _setup(self, portal, current_versions):
        self.tool: MigrationTool = portal.portal_migration
        self.versions = current_versions

    @pytest.mark.parametrize(
        "key,expected",
        [
            [
                "core",
                {
                    "name": "portalbrasil.core",
                    "package_version": "core_package",
                    "instance_version": "current_profile_version",
                    "fs_version": "current_profile_version",
                },
            ],
            ["Zope", "5.13"],
            ["CMFPlone", "6.1.1"],
        ],
    )
    def test_core_versions(self, key: str, expected: str | dict):
        """Test core_versions."""
        if key == "core":
            expected["package_version"] = self.versions.core_package
            expected["instance_version"] = self.versions.core_profile
            expected["fs_version"] = self.versions.core_profile
        info = self.tool.coreVersions()
        assert isinstance(info, dict)
        assert info[key] == expected

    @pytest.mark.parametrize(
        "key",
        [
            "CMF",
            "CMFPlone",
            "Debug mode",
            "PIL",
            "Platform",
            "Plone File System",
            "Plone Instance",
            "core",
            "plone.restapi",
            "plone.volto",
            "Python",
            "Zope",
        ],
    )
    def test_core_versions_keys(self, key: str):
        """Test all keys in version information."""
        info = self.tool.coreVersions()
        assert key in info
