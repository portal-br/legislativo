from . import DISTRIBUTION_INFO
from plone.distribution.core import Distribution
from portalbrasil.legislativo import __version__
from portalbrasil.legislativo.utils import distributions as dist_utils

import pytest


class TestUtilsDistributions:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the Plone site to the test instance."""
        self.portal = portal

    def test_current_distribution(self):
        """The current site was created by the Portal Modelo distribution."""
        result = dist_utils.current_distribution()
        assert isinstance(result, Distribution)
        assert result.name == DISTRIBUTION_INFO["name"]

    def test_distribution_info(self):
        """distribution_info describes the distribution and package version."""
        assert dist_utils.distribution_info() == {
            **DISTRIBUTION_INFO,
            "package_version": __version__,
        }
