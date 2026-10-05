from plone import api
from plone.restapi.services import Service
from portalbrasil.legislativo.tools.migration import MigrationTool
from portalbrasil.legislativo.utils.distributions import distribution_info
from typing import Any


class SystemGet(Service):
    def reply(self) -> dict[str, Any]:
        migration_tool: MigrationTool = api.portal.get_tool("portal_migration")
        core_versions = migration_tool.coreVersions()
        core_info = core_versions["core"]
        gs_fs = core_info.get("fs_version")
        gs_instance = core_info.get("instance_version")
        package_version = core_info.get("package_version")
        package_name = core_info.get("name")
        return {
            "@id": f"{self.context.absolute_url()}/@system",
            "distribution": distribution_info(),
            "core": {
                "name": package_name,
                "version": package_version,
                "profile_version_installed": gs_instance,
                "profile_version_file_system": gs_fs,
            },
            "zope_version": core_versions.get("Zope"),
            "plone_version": core_versions.get("CMFPlone"),
            "plone_restapi_version": core_versions.get("plone.restapi"),
            "plone_volto_version": core_versions.get("plone.volto"),
            "python_version": core_versions.get("Python"),
            "cmf_version": core_versions.get("CMF"),
            "pil_version": core_versions.get("PIL"),
            "debug_mode": core_versions.get("Debug mode"),
            "upgrade": gs_fs != gs_instance,
        }
