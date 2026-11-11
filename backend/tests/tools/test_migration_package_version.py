"""Versions read by the migration tool, without pkg_resources."""

from importlib.metadata import PackageNotFoundError
from portalbrasil.legislativo import __version__
from portalbrasil.legislativo.tools.migration import package_version

import pytest


def test_installed_version():
    """The version of an installed distribution is read from its metadata."""
    assert package_version("portalbrasil.legislativo") == __version__


def test_unknown_distribution_raises():
    """An unknown distribution raises, as pkg_resources did with DistributionNotFound."""
    with pytest.raises(PackageNotFoundError):
        package_version("no-such-distribution")
