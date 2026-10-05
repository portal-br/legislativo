from plone.app.robotframework.autologin import AutoLogin
from plone.app.robotframework.content import Content
from plone.app.robotframework.genericsetup import GenericSetup
from plone.app.robotframework.i18n import I18N
from plone.app.robotframework.mailhost import MockMailHost
from plone.app.robotframework.quickinstaller import QuickInstaller
from plone.app.robotframework.server import Zope2ServerRemote
from plone.app.robotframework.users import Users


RF_LIBRARIES = (
    AutoLogin,
    QuickInstaller,
    GenericSetup,
    Content,
    Users,
    I18N,
    MockMailHost,
    Zope2ServerRemote,
)
