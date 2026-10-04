from plone import api
from Products.GenericSetup.tool import SetupTool


def get_setup_tool() -> SetupTool:
    """Return SetupTool."""
    return api.portal.get_tool("portal_setup")


def sanitize_gs_version(version: str) -> str:
    # Instance version was not pkg_resources compatible...
    version = version.replace("devel (svn/unreleased)", "dev")
    version = version.rstrip("-final")
    version = version.rstrip("final")
    version = version.replace("alpha", "a")
    version = version.replace("beta", "b")
    version = version.replace("-", ".")
    return version


def install_package(package: str, profile: str = "default") -> str:
    """Install a package and return the installed version."""
    st = get_setup_tool()
    profile_id = f"profile-{package}:{profile}"
    st.runAllImportStepsFromProfile(profile_id)
    version: str = st.getLastVersionForProfile(profile_id)
    return version
