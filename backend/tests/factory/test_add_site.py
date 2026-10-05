from plone.distribution.api import distribution as dist_api
from portalbrasil.legislativo import DISTRIBUTION_NAME


class TestAddSiteDefaults:
    def test_distribution(self, site_with_defaults):
        """The Portal Modelo distribution is used by default."""
        report = dist_api.get_creation_report(site_with_defaults)
        assert report.name == DISTRIBUTION_NAME

    def test_default_language(self, site_with_defaults):
        """Brazilian Portuguese is the default language."""
        registry = site_with_defaults.portal_registry
        assert registry["plone.default_language"] == "pt-br"
        assert registry["plone.available_languages"] == ["pt-br"]
