from . import plone_workflow_definition
from collections.abc import Generator
from Products.CMFPlone.Portal import PloneSite
from xml.etree import ElementTree

import pytest


@pytest.fixture(scope="class")
def portal(portal_class: PloneSite) -> Generator[PloneSite]:
    """Yield the class-scoped Plone site for setup tests."""
    yield portal_class


@pytest.fixture(scope="module")
def plone_definition() -> ElementTree.Element:
    """Parse the workflow definition shipped by Products.CMFPlone."""
    # Trusted input: a file inside the installed Products.CMFPlone package.
    return ElementTree.parse(plone_workflow_definition()).getroot()  # noqa: S314
