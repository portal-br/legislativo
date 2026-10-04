from . import BASE_CONTENT
from . import EXAMPLE_CONTENT
from plone import api
from plone.distribution.api import distribution as dist_api
from typing import Any
from typing import ClassVar

import pytest


class TestCreationWithExampleContent:
    @pytest.fixture(autouse=True)
    def _setup(self, portal, answers) -> None:
        """Bind the created site and the answers used to create it."""
        self.portal = portal
        self.answers = answers

    def test_site_id(self):
        """The site gets the requested id."""
        assert self.portal.getId() == self.answers["site_id"]

    @pytest.mark.parametrize(
        "attr,key",
        [
            ("title", "title"),
            ("description", "description"),
        ],
    )
    def test_site_attributes(self, attr: str, key: str):
        """The site title and description come from the answers."""
        assert getattr(self.portal, attr) == self.answers[key]

    @pytest.mark.parametrize(
        "record,key",
        [
            ("plone.site_title", "title"),
            ("plone.email_from_name", "title"),
            ("plone.default_language", "default_language"),
            ("plone.portal_timezone", "portal_timezone"),
        ],
    )
    def test_registry(self, record: str, key: str):
        """Registry records are updated from the answers."""
        assert api.portal.get_registry_record(record) == self.answers[key]

    def test_creation_report(self, distribution_name):
        """The site records which distribution created it."""
        report = dist_api.get_creation_report(self.portal)
        assert report.name == distribution_name

    def test_example_content(self, content_count):
        """The example content is imported."""
        assert content_count() == EXAMPLE_CONTENT


class TestCreationWithoutExampleContent:
    answers_override: ClassVar[dict[str, Any]] = {
        "site_id": "portal-base",
        "setup_content": False,
    }

    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the created site."""
        self.portal = portal

    def test_site_id(self):
        """The site gets the requested id."""
        assert self.portal.getId() == self.answers_override["site_id"]

    def test_base_content(self, content_count):
        """Only the base content is imported."""
        assert content_count() == BASE_CONTENT
