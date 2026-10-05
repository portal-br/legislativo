from . import BEHAVIORS
from . import FTI_VALUES
from . import NAVTITLE_TYPES
from . import TEST_ONLY_BEHAVIORS
from plone.behavior.interfaces import IBehavior
from plone.dexterity.fti import DexterityFTI
from zope.component import queryUtility

import pytest


class TestContentTypeFTI:
    @pytest.fixture(autouse=True)
    def _setup(self, portal, get_fti) -> None:
        """Bind the site and the FTI lookup to the instance."""
        self.portal = portal
        self.get_fti = get_fti

    @pytest.mark.parametrize("portal_type", sorted(FTI_VALUES))
    def test_fti(self, portal_type: str):
        """Test title, class and global_allow of each FTI."""
        title, klass, global_allow = FTI_VALUES[portal_type]
        fti = self.get_fti(portal_type)
        assert isinstance(fti, DexterityFTI)
        assert (fti.title, fti.klass, fti.global_allow) == (title, klass, global_allow)

    @pytest.mark.parametrize("portal_type", sorted(BEHAVIORS))
    def test_behaviors(self, portal_type: str):
        """Test behaviors are present and in the expected order."""
        assert tuple(self.get_fti(portal_type).behaviors) == BEHAVIORS[portal_type]

    @pytest.mark.parametrize("portal_type", sorted(NAVTITLE_TYPES))
    def test_navigation_title(self, portal_type: str):
        """Every content type offers a navigation title."""
        assert "volto.navtitle" in self.get_fti(portal_type).behaviors

    @pytest.mark.parametrize("portal_type", sorted(BEHAVIORS))
    def test_behaviors_registered(self, portal_type: str):
        """Every behavior listed on an FTI is registered."""
        missing = [
            name
            for name in self.get_fti(portal_type).behaviors
            if queryUtility(IBehavior, name=name) is None
        ]
        assert missing == []

    @pytest.mark.parametrize("portal_type", sorted(BEHAVIORS))
    def test_no_test_only_behaviors(self, portal_type: str):
        """FTIs do not use behaviors missing from production installs."""
        behaviors = set(self.get_fti(portal_type).behaviors)
        assert behaviors.isdisjoint(TEST_ONLY_BEHAVIORS)
