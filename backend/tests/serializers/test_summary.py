from . import SUMMARY_METADATA
from plone.restapi.interfaces import IJSONSummarySerializerMetadata
from zope.component import getUtility

import pytest


class TestSummaryMetadata:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the Plone site to the test instance."""
        self.portal = portal

    def test_registered(self):
        """The package registers its summary metadata utility."""
        utility = getUtility(
            IJSONSummarySerializerMetadata,
            name="portalbrasil.legislativo.summary_serializer_metadata",
        )
        assert utility.default_metadata_fields() == SUMMARY_METADATA
