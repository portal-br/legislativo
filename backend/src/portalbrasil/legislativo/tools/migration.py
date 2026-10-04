from AccessControl.class_init import InitializeClass
from App.config import DefaultConfiguration
from App.config import getConfiguration
from plone.base.interfaces import IMigrationTool
from Products.CMFCore.utils import registerToolInterface
from Products.CMFPlone.MigrationTool import MigrationTool as BaseTool
from typing import Any
from zope.interface import implementer

import pkg_resources
import sys


def get_configuration() -> DefaultConfiguration:
    """Return the global Zope configuration object."""
    return getConfiguration()


def package_version(package_name: str) -> str:
    """Return the version of an installed package."""
    package_dist = pkg_resources.get_distribution(package_name)
    version: str = package_dist.version
    return version


@implementer(IMigrationTool)
class MigrationTool(BaseTool):
    """Custom migration tool that extends the default Plone one."""

    def coreVersions(self) -> dict[str, Any]:
        """Return core versions of the system and the migration tool."""
        config = get_configuration()
        # Useful core information.
        plone_version = package_version("Products.CMFPlone")
        instance_version = self.getInstanceVersion()
        fs_version = self.getFileSystemVersion()
        return {
            "Python": sys.version,
            "Zope": package_version("Zope"),
            "Platform": sys.platform,
            "plone.restapi": package_version("plone.restapi"),
            "plone.volto": package_version("plone.volto"),
            "CMFPlone": plone_version,
            "Plone": plone_version,
            "Plone Instance": instance_version,
            "Plone File System": fs_version,
            "CMF": package_version("Products.CMFCore"),
            "Debug mode": "Yes" if config.debug_mode else "No",
            "PIL": package_version("pillow"),
            "core": {
                "name": self.get_package_name(),
                "package_version": self.getSoftwareVersion(),
                "instance_version": instance_version,
                "fs_version": fs_version,
            },
        }


InitializeClass(MigrationTool)
registerToolInterface("portal_migration", IMigrationTool)
