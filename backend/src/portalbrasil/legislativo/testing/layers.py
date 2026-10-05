from OFS.Application import Application
from plone.app.testing.interfaces import SITE_OWNER_NAME
from plone.app.testing.interfaces import SITE_OWNER_PASSWORD
from plone.app.testing.interfaces import TEST_USER_ID
from plone.app.testing.interfaces import TEST_USER_NAME
from plone.app.testing.interfaces import TEST_USER_PASSWORD
from plone.app.testing.interfaces import TEST_USER_ROLES
from plone.app.testing.layers import PloneFixture
from plone.testing import zope
from typing import Any
from zope.globalrequest import setRequest


PLONE_SITE_TITLE = "Câmara Modelo"

DEFAULT_ANSWERS = {
    "site_id": "plone",
    "title": PLONE_SITE_TITLE,
    "description": "Site da câmara modelo",
    "available_languages": ["pt-br"],
    "default_language": "pt-br",
    "portal_timezone": "America/Sao_Paulo",
    "setup_content": True,
}


class PBFixture(PloneFixture):
    package_name: str = "portalbrasil.legislativo"
    internal_packages: tuple[str, ...] = (
        "plone.restapi",
        "plone.volto",
    )

    @property
    def products(self) -> tuple[tuple[str, dict[str, Any]], ...]:
        products = list(super().products)
        for package in self.internal_packages:
            products.append((package, {"loadZCML": True}))
        # Add current package
        products.append((self.package_name, {"loadZCML": True}))
        return tuple(products)


class PBDistributionFixture(PBFixture):
    sites: tuple[tuple[str, dict[str, Any]], ...] = ()

    def setUpDefaultContent(self, app: Application) -> None:
        """Create a Plone site using plone.distribution."""
        from portalbrasil.legislativo.factory import add_site

        # Create the owner user and "log in" so that the site object gets
        # the right ownership information
        app["acl_users"].userFolderAddUser(
            SITE_OWNER_NAME, SITE_OWNER_PASSWORD, ["Manager"], []
        )

        setRequest(app.REQUEST)
        zope.login(app["acl_users"], SITE_OWNER_NAME)
        sites = self.sites
        if not sites:
            raise RuntimeError("No sites defined in this fixture")

        for distribution_name, answers in sites:
            site_id = answers["site_id"]
            # Create Plone site
            add_site(
                app,
                extension_ids=self.extensionProfiles,
                distribution=distribution_name,
                **answers,
            )
            # Create the test user. (Plone)PAS does not have an API to create a
            # user with different userid and login name, so we call the plugin
            # directly.
            pas = app[site_id]["acl_users"]
            pas.source_users.addUser(TEST_USER_ID, TEST_USER_NAME, TEST_USER_PASSWORD)
            for role in TEST_USER_ROLES:
                pas.portal_role_manager.doAssignRoleToPrincipal(TEST_USER_ID, role)

        # Log out again
        zope.logout()
        setRequest(None)


class LegislativoFixture(PBDistributionFixture):
    sites = (("portalmodelo", DEFAULT_ANSWERS),)
    internal_packages: tuple[str, ...] = (
        "plone.restapi",
        "plone.volto",
    )
