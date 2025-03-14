from pathlib import Path
from plonegovbr.portal_leg.utils.scripts import parse_answers

import pytest


@pytest.fixture
def answers_file():
    path = Path(__file__).parent / "default.json"
    return path


@pytest.mark.parametrize(
    "key,value,expected",
    (
        ("site_id", "", "Plone"),
        ("site_id", "Site", "Site"),
        ("title", "Foo Bar", "Foo Bar"),
        ("description", "A new site", "A new site"),
        (
            "description",
            "",
            "Site da câmara modelo",
        ),
        ("default_language", "", "pt-br"),
        ("default_language", "de", "de"),
        ("portal_timezone", "", "America/Sao_Paulo"),
        ("portal_timezone", "UTC", "UTC"),
        ("setup_content", "", True),
        ("setup_content", "f", False),
    ),
)
def test_parse_answers(answers_file, key: str, value: str, expected: str | bool):
    answers = {key: value}
    result = parse_answers(answers_file, answers)
    assert result[key] == expected
