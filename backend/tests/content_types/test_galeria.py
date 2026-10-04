from collections.abc import Callable
from plone import api
from plone.dexterity.content import DexterityContent
from portalbrasil.legislativo.content.galeria import Galeria
from portalbrasil.legislativo.content.galeria import IGaleria

import pytest


@pytest.fixture(scope="class")
def portal_type() -> str:
    return "Galeria"


@pytest.fixture(scope="class")
def payload(portal_type: str) -> dict:
    return {
        "type": portal_type,
        "id": "galeria-de-fotos",
        "title": "Galeria de fotos",
        "description": "Fotos da sessão solene",
    }


class TestGaleriaFTI:
    @pytest.fixture(autouse=True)
    def _setup(self, portal, get_fti, portal_type: str) -> None:
        """Bind the site and the FTI of the type under test to the instance."""
        self.portal = portal
        self.fti = get_fti(portal_type)

    @pytest.mark.parametrize(
        "attr,expected",
        [
            ("description", "A gallery of photos"),
            ("allow_discussion", True),
            ("filter_content_types", True),
            ("allowed_content_types", ("Image",)),
            ("add_permission", "portalbrasil.legislativo.galeria.add"),
            ("schema", "portalbrasil.legislativo.content.galeria.IGaleria"),
        ],
    )
    def test_fti(self, attr: str, expected):
        """Test FTI values not covered by test_ct_fti."""
        assert getattr(self.fti, attr) == expected


class TestGaleriaContent:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the site to the instance."""
        self.portal = portal

    def test_create(self, content_instance: DexterityContent, portal_type: str):
        """A Galeria is created with its class and schema."""
        assert content_instance.portal_type == portal_type
        assert isinstance(content_instance, Galeria)
        assert IGaleria.providedBy(content_instance)

    def test_add_image(self, content_instance: DexterityContent):
        """A Galeria accepts images."""
        with api.env.adopt_roles(["Manager"]):
            image = api.content.create(
                container=content_instance, type="Image", id="foto"
            )
        assert image.portal_type == "Image"

    @pytest.mark.parametrize("child_type", ["Document", "File", "Galeria"])
    def test_disallowed_types(
        self, content_instance: DexterityContent, child_type: str
    ):
        """A Galeria accepts nothing but images."""
        with (
            api.env.adopt_roles(["Manager"]),
            pytest.raises(api.exc.InvalidParameterError),
        ):
            api.content.create(container=content_instance, type=child_type, id="item")

    def test_displayed_in_navigation(
        self, displayed_types: tuple[str, ...], portal_type: str
    ):
        """Galeria is listed in the navigation."""
        assert portal_type in displayed_types

    @pytest.mark.parametrize(
        "role,expected",
        [
            ("Manager", True),
            ("Site Administrator", True),
            ("Owner", True),
            ("Contributor", True),
            ("Editor", False),
            ("Reader", False),
            ("Anonymous", False),
        ],
    )
    def test_add_permission(
        self,
        roles_with_permission: Callable[[str], list[str]],
        role: str,
        expected: bool,
    ):
        """Only roles that add content may add a Galeria."""
        roles = roles_with_permission("portalbrasil.legislativo: Add Galeria")
        assert (role in roles) is expected


class TestGaleriaVersioning:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the site to the instance."""
        self.portal = portal

    def test_versionable(self, portal_type: str, versionable_content_types: list[str]):
        """The type is registered in portal_repository."""
        assert portal_type in versionable_content_types

    def test_create_initial_version_after_adding(
        self, last_version, content_instance: DexterityContent
    ):
        """Adding content creates version 0."""
        version = last_version(content_instance)
        assert version.comment.default == "Initial version"
        assert version.version_id == 0

    def test_create_version_on_save(
        self,
        notify_modified,
        history,
        last_version,
        content_instance: DexterityContent,
    ):
        """Modifying content creates a new version."""
        with api.env.adopt_roles(["Manager"]):
            content_instance.title = "Galeria de fotos atualizada"
            notify_modified(content_instance)
        assert len(history(content_instance)) == 2
        version = last_version(content_instance)
        assert version.comment is None
        assert version.version_id == 1
