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
