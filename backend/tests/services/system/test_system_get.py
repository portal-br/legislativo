from . import DISTRIBUTION
from . import VALUES
from portalbrasil.legislativo import __version__
from portalbrasil.legislativo import PACKAGE_NAME

import pytest


class TestSystemGet:
    @pytest.fixture(autouse=True)
    def _setup(self, api_manager_request, current_versions) -> None:
        """Bind the authenticated API session and profile version to the test."""
        self.api_session = api_manager_request
        self.profile_version = current_versions.base

    def get(self) -> dict:
        """Return the decoded @system response."""
        return self.api_session.get("/@system").json()

    @pytest.mark.parametrize(
        "key,type_",
        (
            ("@id", str),
            ("cmf_version", str),
            ("debug_mode", str),
            ("distribution", dict),
            ("pil_version", str),
            ("plone_restapi_version", str),
            ("plone_version", str),
            ("plone_volto_version", str),
            ("core", dict),
            ("python_version", str),
            ("upgrade", bool),
        ),
    )
    def test_keys(self, key: str, type_: type):
        """The response has the expected keys and types."""
        assert isinstance(self.get()[key], type_)

    @pytest.mark.parametrize("key", sorted(VALUES))
    def test_values(self, key: str):
        """Versions and flags match the pinned stack."""
        assert self.get()[key] == VALUES[key]

    def test_core(self):
        """The core section describes this package and its base profile."""
        assert self.get()["core"] == {
            "name": PACKAGE_NAME,
            "version": __version__,
            "profile_version_installed": self.profile_version,
            "profile_version_file_system": self.profile_version,
        }

    @pytest.mark.parametrize("key", sorted(DISTRIBUTION))
    def test_distribution(self, key: str):
        """The distribution section describes the Portal Modelo."""
        assert self.get()["distribution"][key] == DISTRIBUTION[key]
