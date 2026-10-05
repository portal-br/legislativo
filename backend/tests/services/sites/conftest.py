from collections.abc import Callable
from collections.abc import Generator
from plone.restapi.testing import RelativeSession
from typing import Any

import pytest


@pytest.fixture()
def app(functional: dict[str, Any]) -> Generator[Any]:
    """Yield the Zope application root."""
    yield functional["app"]


@pytest.fixture()
def request_api_factory(app: Any) -> Callable[[], RelativeSession]:
    """Return a helper that builds a JSON REST API session at the app root."""

    def factory() -> RelativeSession:
        """Build a REST API session accepting ``application/json``."""
        session = RelativeSession(app.absolute_url())
        session.headers.update({"Accept": "application/json"})
        return session

    return factory
