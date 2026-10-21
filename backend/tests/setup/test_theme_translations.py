from gettext import GNUTranslations
from pathlib import Path
from pythongettext.msgfmt import Msgfmt

import pytest
import sc.voltolighttheme


DOMAIN = "sc.voltolighttheme"


@pytest.fixture(scope="module")
def catalog() -> GNUTranslations:
    """Compile, in memory, the pt_BR catalog shipped by the theme.

    The theme wheel may ship stale .mo files, and zope.i18n recompiles them
    only when the .po is newer, so the test reads the .po itself. The Docker
    image compiles every catalog at build time.
    """
    base = Path(sc.voltolighttheme.__file__).parent
    po = base / "locales" / "pt_BR" / "LC_MESSAGES" / f"{DOMAIN}.po"
    return GNUTranslations(Msgfmt(str(po), name=DOMAIN).getAsFile())


@pytest.mark.parametrize(
    "msgid,expected",
    [
        ("Header settings", "Configurações do cabeçalho"),
        ("Footer address", "Rodapé: Endereço"),
        ("Accent Colors", "Cores de destaque"),
        ("Simples Consultoria VLT: Install", "Simples Consultoria VLT: Instalação"),
        (
            "A festive theme with Inter typography and rounded borders.",
            "Um tema festivo com tipografia Inter e bordas arredondadas.",
        ),
    ],
)
def test_pt_br(catalog: GNUTranslations, msgid: str, expected: str):
    """The theme settings are translated into Brazilian Portuguese."""
    assert catalog.gettext(msgid) == expected
