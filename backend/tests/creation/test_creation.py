from plone import api
from plone.app.testing.interfaces import SITE_OWNER_NAME
from plone.distribution.api import site as site_api
from Products.CMFCore.WorkflowCore import WorkflowException
from Products.CMFPlone.Portal import PloneSite
from zope.component.hooks import setSite

import pytest


@pytest.fixture()
def answers():
    return {
        "site_id": "portal",
        "title": "Câmara Modelo",
        "description": "Site da Câmara Modelo",
        "default_language": "pt-br",
        "portal_timezone": "America/Sao_Paulo",
        "setup_content": True,
    }


@pytest.fixture
def create_site(app, distribution_name):
    def func(answers: dict) -> PloneSite:
        with api.env.adopt_user(SITE_OWNER_NAME):
            site = site_api.create(
                app, distribution_name, answers, profile_id="portalbrasil.core:base"
            )
            setSite(site)
        return site

    return func


class TestCreationSite:
    @pytest.fixture(autouse=True)
    def _create_site(self, create_site, answers):
        self.site = create_site(answers)

    @pytest.mark.parametrize(
        "attr,expected",
        [
            ["id", "portal"],
        ],
    )
    def test_properties(self, attr, expected):
        site = self.site
        assert getattr(site, attr) == expected

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["plone.site_title", "Câmara Modelo"],
        ],
    )
    def test_registry_entries(self, key, expected):
        assert api.portal.get_registry_record(key) == expected

    @pytest.mark.parametrize(
        "path,title,portal_type,review_state",
        [
            ("/", "Câmara Modelo", "Plone Site", ""),
        ],
    )
    def test_content_created(self, path, title, portal_type, review_state):
        with api.env.adopt_user(SITE_OWNER_NAME):
            content = api.content.get(path=path)
        assert content.title == title
        assert content.portal_type == portal_type
        if review_state:
            assert api.content.get_state(content) == review_state
        else:
            with pytest.raises(WorkflowException) as exc:
                api.content.get_state(content)
            assert "No workflow provides" in str(exc)
