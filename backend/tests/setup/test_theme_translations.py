from zope.i18n import translate

import pytest


DOMAIN = "sc.voltolighttheme"


class TestThemeTranslations:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Load the site, and with it the translation catalogs."""
        self.portal = portal

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
    def test_pt_br(self, msgid: str, expected: str):
        """The theme settings are translated into Brazilian Portuguese."""
        assert translate(msgid, domain=DOMAIN, target_language="pt_BR") == expected
