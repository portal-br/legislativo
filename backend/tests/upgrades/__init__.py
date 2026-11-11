"""Testes da migração de sites existentes."""

#: Add-on profiles upgraded by ``portal_migration.upgrade``, in this order.
UPGRADED_PROFILES = (
    "plone.restapi:default",
    "plone.volto:default",
    "sc.voltolighttheme:default",
    "plonegovbr.socialmedia:default",
    "plone.formblock:default",
    "portalbrasil.legislativo:default",
)

#: Add-on profiles left out of the upgrade.
NOT_UPGRADED_PROFILES = ("kitconcept.voltolighttheme:default",)
