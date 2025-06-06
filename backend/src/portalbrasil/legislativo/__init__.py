"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "4.0.0a3"

PACKAGE_NAME = "portalbrasil.legislativo"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
