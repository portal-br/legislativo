from collections import Counter
from collections.abc import Callable
from collections.abc import Generator
from Products.CMFPlone.Portal import PloneSite
from typing import Any

import pytest


@pytest.fixture(scope="class")
def portal(
    request: pytest.FixtureRequest,
    app_class: Any,
    create_site: Callable[..., PloneSite],
    prepare_answers: Callable[[], dict[str, Any]],
) -> Generator[PloneSite]:
    """Yield a freshly created Plone site.

    A test class may set ``answers_override`` to change the default answers.
    """
    answers = prepare_answers()
    answers.update(getattr(request.cls, "answers_override", {}))
    site = create_site(app=app_class, answers=answers)
    yield site


@pytest.fixture()
def content_count(portal: PloneSite) -> Callable[[], dict[str, int]]:
    """Return a helper that counts the site objects per portal type."""

    def func() -> dict[str, int]:
        """Count catalogued objects under the site, per portal type."""
        path = "/".join(portal.getPhysicalPath())
        brains = portal.portal_catalog.unrestrictedSearchResults(path=path)
        return dict(Counter(brain.portal_type for brain in brains))

    return func
