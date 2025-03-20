from pathlib import Path
from plone import api
from plone.exportimport import importers
from portalbrasil.legislativo import logger
from Products.GenericSetup.tool import SetupTool


BASE_CONTENT_FOLDER = Path(__file__).parent / "basecontent"


def create_base_content(portal_setup: SetupTool):
    """Import content available at the basecontent folder."""
    portal = api.portal.get()
    importer = importers.get_importer(portal)
    for line in importer.import_site(BASE_CONTENT_FOLDER):
        logger.info(line)
