from plone import api

import pytest


class TestAddonsList:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the class-scoped Plone site to the test instance."""
        self.portal = portal

    def test_addons_list_should_be_empty(self) -> None:
        """Test that the add-on control panel lists no installable add-ons."""
        with api.env.adopt_roles(["Manager"]):
            addons = api.addon.get_addons()
        assert addons == []
