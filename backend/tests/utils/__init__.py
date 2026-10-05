"""Testes dos utilitários."""

from pathlib import Path


#: Answers file used by the site creation script tests.
ANSWERS_FILE = Path(__file__).parent / "default.json"

DISTRIBUTION_INFO = {
    "name": "portalmodelo",
    "title": "Portal Modelo",
    "package_name": "portalbrasil.legislativo.distributions",
}
