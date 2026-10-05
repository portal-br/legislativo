from . import ANSWERS_FILE
from portalbrasil.legislativo import DISTRIBUTION_NAME
from portalbrasil.legislativo import PACKAGE_NAME
from portalbrasil.legislativo.utils import scripts
from typing import Any

import logging
import pytest


@pytest.mark.parametrize(
    "key,value,expected",
    (
        ("site_id", "", "Plone"),
        ("site_id", "Site", "Site"),
        ("title", "", "Câmara Modelo"),
        ("title", "Foo Bar", "Foo Bar"),
        ("description", "", "Site da câmara modelo"),
        ("description", "A new site", "A new site"),
        ("available_languages", "", ["pt-br"]),
        ("available_languages", ["pt-br", "en"], ["pt-br", "en"]),
        ("default_language", "", "pt-br"),
        ("default_language", "en", "en"),
        ("portal_timezone", "", "America/Sao_Paulo"),
        ("portal_timezone", "UTC", "UTC"),
        ("setup_content", "", True),
        ("setup_content", "f", False),
        ("setup_content", "t", True),
        ("setup_content", "  ", True),
        # get_environmental_variables already coerces SITE_SETUP_CONTENT
        ("setup_content", False, False),
        ("setup_content", True, True),
    ),
)
def test_parse_answers(key: str, value: Any, expected: Any):
    """Environment values override the answers file, when present."""
    result = scripts.parse_answers(ANSWERS_FILE, {key: value})
    assert result[key] == expected


@pytest.mark.parametrize(
    "value,expected",
    (
        (None, False),
        (True, True),
        (False, False),
        ("t", True),
        ("true", True),
        ("TRUE", True),
        ("y", True),
        ("yes", True),
        ("on", True),
        ("1", True),
        ("  yes  ", True),
        ("", False),
        ("f", False),
        ("false", False),
        ("no", False),
        ("0", False),
        ("maybe", False),
    ),
)
def test_as_bool(value: Any, expected: bool):
    """Values are coerced into booleans."""
    assert scripts.as_bool(value) is expected


@pytest.mark.parametrize(
    "value,expected",
    (
        ("", []),
        (None, []),
        ("en", ["en"]),
        ("en,de,fr", ["en", "de", "fr"]),
        ("en, de, fr", ["en", "de", "fr"]),
        ("  en ,  de ", ["en", "de"]),
        ("en,", ["en", ""]),
    ),
)
def test_as_list(value: Any, expected: list[str]):
    """Comma separated values are split and trimmed."""
    assert scripts.as_list(value) == expected


def test_options_keys():
    """Only site options are read from the environment."""
    assert [key for key, _, _ in scripts.OPTIONS] == [
        "site_id",
        "title",
        "description",
        "available_languages",
        "default_language",
        "portal_timezone",
        "setup_content",
    ]


@pytest.mark.parametrize("value,expected", (("false", False), ("1", True)))
def test_parse_answers_from_environment(monkeypatch, value: str, expected: bool):
    """Answers read from the environment can be parsed."""
    for _, env_var, _ in scripts.OPTIONS:
        monkeypatch.delenv(env_var, raising=False)
    monkeypatch.setenv("SITE_SETUP_CONTENT", value)
    env_answers = scripts.get_environmental_variables()
    result = scripts.parse_answers(ANSWERS_FILE, env_answers)
    assert result["setup_content"] is expected


class TestGetEnvironmentalVariables:
    @pytest.fixture(autouse=True)
    def _clean_env(self, monkeypatch) -> None:
        """Remove every option variable from the environment."""
        for _, env_var, _ in scripts.OPTIONS:
            monkeypatch.delenv(env_var, raising=False)

    def test_empty_when_no_env_vars(self):
        """No relevant variables set yields an empty mapping."""
        assert scripts.get_environmental_variables() == {}

    def test_plain_value(self, monkeypatch):
        monkeypatch.setenv("SITE_ID", "Plone")
        assert scripts.get_environmental_variables() == {"site_id": "Plone"}

    def test_empty_string_is_kept(self, monkeypatch):
        """An explicitly empty variable is included."""
        monkeypatch.setenv("SITE_TITLE", "")
        assert scripts.get_environmental_variables() == {"title": ""}

    def test_as_list_transform(self, monkeypatch):
        monkeypatch.setenv("SITE_AVAILABLE_LANGUAGES", "en, de")
        assert scripts.get_environmental_variables() == {
            "available_languages": ["en", "de"]
        }

    @pytest.mark.parametrize("value,expected", (("1", True), ("false", False)))
    def test_as_bool_transform(self, monkeypatch, value: str, expected: bool):
        monkeypatch.setenv("SITE_SETUP_CONTENT", value)
        assert scripts.get_environmental_variables()["setup_content"] is expected

    def test_nested_keys(self):
        """Option keys with a dot are expanded into nested mappings."""
        options = (("group.key", "SITE_GROUP_KEY", None),)
        with pytest.MonkeyPatch.context() as mp:
            mp.setenv("SITE_GROUP_KEY", "value")
            result = scripts.get_environmental_variables(options)
        assert result == {"group": {"key": "value"}}


class TestCreateSite:
    @pytest.fixture(autouse=True)
    def _setup(self, app, monkeypatch) -> None:
        """Bind the Zope app root and clear the option variables."""
        self.app = app
        for _, env_var, _ in scripts.OPTIONS:
            monkeypatch.delenv(env_var, raising=False)

    def _create_site(self):
        """Call :func:`create_site` with the answers file of this package."""
        return scripts.create_site(
            app=self.app,
            answers_file=ANSWERS_FILE,
            env_answers={},
            package_iface=None,
        )

    def test_create_site(self):
        """A site is created from the answers file."""
        site = self._create_site()
        assert site.id == "Plone"

    def test_create_site_uses_distribution(self, caplog):
        """The distribution is always the Portal Modelo one."""
        with caplog.at_level(logging.INFO, logger=PACKAGE_NAME):
            self._create_site()
        assert f" - Usando a distribuição {DISTRIBUTION_NAME}" in caplog.text
