from plone import api

import pytest


PREFIX = "sc.voltolighttheme.theme.default"


class TestDefaultTheme:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the site to the instance."""
        self.portal = portal

    @pytest.mark.parametrize(
        "key,expected",
        [
            ("name", "Portal Modelo Base"),
            ("font_family_primary", "Inter, sans-serif"),
            ("primary_accent_color_light", "#009c3b"),
            ("secondary_accent_color_light", "#002671"),
            ("accent_color_light", "#ffe122"),
        ],
    )
    def test_default_theme(self, key: str, expected: str):
        """The default block theme uses the Portal Modelo colors."""
        assert api.portal.get_registry_record(f"{PREFIX}.{key}") == expected
