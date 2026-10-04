"""Tipo de conteúdo Galeria."""

from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from zope.interface import implementer


class IGaleria(Schema):
    """Schema da Galeria: os campos vêm dos behaviors da FTI."""


@implementer(IGaleria)
class Galeria(Container):
    """Galeria de fotos: um container de imagens."""
