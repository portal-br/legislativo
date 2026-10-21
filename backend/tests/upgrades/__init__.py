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

#: plone.volto 6.0.1 registers upgrade steps from 1100 to 1101, but its
#: metadata.xml still declares version 1100, so a new site starts with them
#: pending.
PROFILES_WITH_PENDING_UPGRADES = ("plone.volto:default",)
