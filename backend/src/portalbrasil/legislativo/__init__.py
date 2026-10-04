"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "4.0.0a3"

PACKAGE_NAME = "portalbrasil.legislativo"
DEFAULT_PROFILE = f"{PACKAGE_NAME}:base"
CMF_DEPENDENCIES_PROFILE = f"{PACKAGE_NAME}:cmfdependencies"
LEGISLATIVO_PROFILE = f"{PACKAGE_NAME}:default"
DISTRIBUTION_NAME = "portalmodelo"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)


def initialize(context: object) -> None:
    """Register the package tools with Zope.

    :param context: Zope product context passed by ``Products`` initialization.
    """
    from portalbrasil.legislativo.tools import migration
    from Products.CMFPlone.utils import ToolInit

    tools = (migration.MigrationTool,)
    ToolInit(
        "Plone Tool",
        tools=tools,
        icon="tool.gif",
    ).initialize(context)
