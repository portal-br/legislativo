from collections.abc import Generator
from Products.CMFPlone.Portal import PloneSite

import pytest


@pytest.fixture(scope="class")
def portal(portal_class: PloneSite) -> Generator[PloneSite]:
    """Yield the class-scoped Plone site for content-type tests."""
    yield portal_class
