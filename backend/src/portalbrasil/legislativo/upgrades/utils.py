"""Helpers shared by the upgrade steps."""

from portalbrasil.legislativo import logger
from Products.GenericSetup.tool import SetupTool


def null_upgrade_step(setup_tool: SetupTool) -> None:
    """Do nothing: the version bump alone lets the migration tool run the add-on list.

    :param setup_tool: The ``portal_setup`` tool.
    """
    logger.info("Null upgrade step: the add-on list runs after the base profile")
