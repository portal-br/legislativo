from . import BASE_PROFILE_ID
from copy import deepcopy

import pytest


class TestSitesEndpoint:
    @pytest.fixture(autouse=True)
    def _setup(self, api_manager_request, distribution_name) -> None:
        """Bind the API session and the @sites endpoint URL to the test."""
        self.api_session = api_manager_request
        self.url = f"@sites/{distribution_name}"

    def test_get(self):
        """The distribution is exposed by the @sites endpoint."""
        response = self.api_session.get(self.url)
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    @pytest.mark.parametrize("key", ("languages", "timezones"))
    def test_get_definitions(self, key: str):
        """The schema carries the definitions used by its fields."""
        response = self.api_session.get(self.url)
        definitions = response.json().get("schema", {}).get("definitions", {})
        assert key in definitions

    def test_post(self, answers):
        """A site is created through the overridden endpoint."""
        payload = deepcopy(answers)
        payload["site_id"] = "plone-api"
        response = self.api_session.post(self.url, json=payload)
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == payload["site_id"]
        assert data["_profile_id"] == BASE_PROFILE_ID
