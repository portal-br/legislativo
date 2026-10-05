"""Testes de instalação e configuração do site."""

from pathlib import Path


#: Profiles that must be installed on a site created by the distribution.
#: ``plone.outputfilters:default`` is left out: it has no metadata.xml and no
#: import steps, so GenericSetup records neither a version nor an import date.
INSTALLED_PROFILES = (
    "Products.MimetypesRegistry:MimetypesRegistry",
    "Products.PortalTransforms:PortalTransforms",
    "Products.CMFEditions:CMFEditions",
    "Products.PlonePAS:PlonePAS",
    "plone.app.linkintegrity:default",
    "plone.app.registry:default",
    "plone.app.theming:default",
    "plone.app.users:default",
    "plone.protect:default",
    "plone.staticresources:default",
    "plone.app.contenttypes:default",
    "plone.restapi:default",
    "plone.volto:default",
    "plonetheme.barceloneta:default",
    "sc.voltolighttheme:default",
    "plone.formblock:default",
    "plonegovbr.socialmedia:default",
)

#: Profiles that must not be installed: replaced add-ons and intranet-only setup.
UNINSTALLED_PROFILES = (
    "collective.volto.formsupport:default",
    "collective.honeypot:default",
    "sc.voltolighttheme:intranet",
    "pas.plugins.oidc:default",
    "pas.plugins.authomatic:default",
    "pas.plugins.keycloakgroups:default",
)

WORKFLOW_ID = "simple_publication_workflow"

#: Types bound to no workflow, as in Plone's default profile.
TYPES_WITHOUT_WORKFLOW = ("File", "Image", "Plone Site")

#: Types bound to the default chain.
TYPES_WITH_DEFAULT_WORKFLOW = (
    "Collection",
    "Document",
    "Event",
    "Folder",
    "Link",
    "News Item",
)


def plone_workflow_definition() -> Path:
    """Return the path of the workflow definition shipped by Products.CMFPlone."""
    import Products.CMFPlone

    base = Path(Products.CMFPlone.__file__).parent
    return base / "profiles" / "default" / "workflows" / WORKFLOW_ID / "definition.xml"
