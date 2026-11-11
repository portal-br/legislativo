from portalbrasil.legislativo import __version__
from portalbrasil.legislativo.utils import packages as pkg_utils

import pytest


@pytest.mark.parametrize(
    "package_name,expected",
    [
        ("portalbrasil.legislativo", __version__),
        ("portalbrasil.legislativo.testing", __version__),
        ("", "-"),
    ],
)
def test_package_version(package_name: str, expected: str):
    """Package versions resolve, including for sub packages."""
    assert pkg_utils.package_version(package_name) == expected


@pytest.mark.parametrize(
    "package_name,expected",
    [
        ("portalbrasil.legislativo.no_such_module", __version__),
        ("no-such-distribution", "-"),
    ],
)
def test_package_version_not_found(package_name: str, expected: str):
    """An unknown name falls back to its parent package, or to ``-``."""
    assert pkg_utils.package_version(package_name) == expected
