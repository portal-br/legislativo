"""Service to create a Plone Site."""

from plone.distribution import logger
from plone.distribution.api import distribution as dist_api
from plone.distribution.api import site as site_api
from plone.distribution.services.sites.add import SiteCreate as BaseService
from plone.distribution.utils.validation import validate_answers
from plone.restapi.deserializer import json_body
from typing import Any
from zExceptions import BadRequest
from zExceptions import NotFound
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse

import plone.protect.interfaces


@implementer(IPublishTraverse)
class SiteCreate(BaseService):
    profile_id: str = "portalbrasil.legislativo:base"

    def reply(self) -> dict[str, Any]:
        # Disable CSRF protection
        if "IDisableCSRFProtection" in dir(plone.protect.interfaces):
            alsoProvides(self.request, plone.protect.interfaces.IDisableCSRFProtection)
        data = json_body(self.request)
        distribution_name = (
            self.params[0] if self.params else data.get("distribution", "default")
        )
        self.errors: list[str] = []
        # Get distribution
        try:
            distribution = dist_api.get(distribution_name)
        except ValueError:
            raise NotFound(f"No distribution named {distribution_name}.") from None

        # Validate answers
        if not validate_answers(answers=data, schema=distribution.schema):
            raise BadRequest("Invalid data for site creation.")

        try:
            site = site_api.create(
                self.context,
                distribution_name=distribution_name,
                answers=data,
                profile_id=self.profile_id,
            )
        except KeyError:
            logger.error("Error creating the site.", exc_info=True)
            raise BadRequest("Error creating the site.") from None
        site_info = {
            "@id": site.absolute_url(),
            "@type": site.portal_type,
            "id": site.id,
            "title": site.title,
            "description": site.description,
            "_profile_id": self.profile_id,
        }
        return site_info
