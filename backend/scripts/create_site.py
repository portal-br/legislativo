from pathlib import Path
from portalbrasil.legislativo.interfaces import IBrowserLayer
from portalbrasil.legislativo.utils import scripts

import os


SCRIPT_DIR = Path().cwd() / "scripts"


def main():
    app = globals()["app"]
    filename = os.getenv("ANSWERS", "default.json")
    answers_file = SCRIPT_DIR / filename
    scripts.create_site(
        app=app,
        answers_file=answers_file,
        env_answers={},
        package_iface=[IBrowserLayer],
    )


if __name__ == "__main__":
    main()
