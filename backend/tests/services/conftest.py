from collections.abc import Callable
from collections.abc import Generator
from plone.app.testing import SITE_OWNER_NAME
from plone.app.testing import SITE_OWNER_PASSWORD
from plone.restapi.testing import RelativeSession
from Products.CMFPlone.Portal import PloneSite
from typing import Any

import pytest


@pytest.fixture()
def portal(functional: dict[str, Any]) -> Generator[PloneSite]:
    """Yield the function-scoped functional Plone site."""
    yield functional["portal"]


@pytest.fixture()
def request_api_factory(portal: PloneSite) -> Callable[[], RelativeSession]:
    """Return a helper that builds a REST API session bound to the site."""

    def factory() -> RelativeSession:
        """Build a REST API session targeting the ``++api++`` traverser."""
        url = portal.absolute_url()
        return RelativeSession(f"{url}/++api++")

    return factory


@pytest.fixture()
def api_manager_request(
    request_api_factory: Callable[[], RelativeSession],
) -> Generator[RelativeSession]:
    """Yield a REST API session authenticated as the site owner (Manager)."""
    request = request_api_factory()
    request.auth = (SITE_OWNER_NAME, SITE_OWNER_PASSWORD)
    yield request
    request.auth = ()
