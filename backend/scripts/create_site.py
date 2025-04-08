from pathlib import Path
from portalbrasil.core.utils.scripts import create_site
from portalbrasil.legislativo.interfaces import IBrowserLayer

import os


SCRIPT_DIR = Path().cwd() / "scripts"

# ANSWERS OVERRIDE
ANSWERS = {
    "site_id": os.getenv("SITE_ID"),
    "title": os.getenv("SITE_TITLE"),
    "description": os.getenv("SITE_DESCRIPTION"),
    "default_language": os.getenv("SITE_DEFAULT_LANGUAGE"),
    "portal_timezone": os.getenv("SITE_PORTAL_TIMEZONE"),
    "setup_content": os.getenv("SITE_SETUP_CONTENT", "true"),
}


def main():
    app = globals()["app"]
    filename = os.getenv("ANSWERS", "default.json")
    answers_file = SCRIPT_DIR / filename
    create_site(app, ANSWERS, answers_file, IBrowserLayer)


if __name__ == "__main__":
    main()
