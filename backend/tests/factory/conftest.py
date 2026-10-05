from . import SITE_ID
from collections.abc import Generator
from OFS.Application import Application
from plone.app.testing.interfaces import SITE_OWNER_NAME
from plone.testing import zope
from portalbrasil.legislativo.factory import add_site
from Products.CMFPlone.Portal import PloneSite

import pytest


@pytest.fixture(scope="class")
def site_with_defaults(functional_app_class: Application) -> Generator[PloneSite]:
    """Create a site, as the site owner, passing only the site id to add_site."""
    app = functional_app_class
    zope.login(app["acl_users"], SITE_OWNER_NAME)
    try:
        yield add_site(app, site_id=SITE_ID)
    finally:
        zope.logout()
