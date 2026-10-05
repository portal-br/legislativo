from plone.app.robotframework.remote import RemoteLibraryLayer
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE
from portalbrasil.legislativo.testing import layers
from portalbrasil.legislativo.testing import robot


PB_FIXTURE = layers.LegislativoFixture()


class Layer(PloneSandboxLayer):
    defaultBases = (PB_FIXTURE,)


FIXTURE = Layer()

INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="portalbrasil.legislativoLayer:IntegrationTesting",
)


FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE, WSGI_SERVER_FIXTURE),
    name="portalbrasil.legislativoLayer:FunctionalTesting",
)

REMOTE_LIBRARY_BUNDLE_FIXTURE = RemoteLibraryLayer(
    bases=(PB_FIXTURE,),
    libraries=robot.RF_LIBRARIES,
    name="RemoteLibraryBundle:RobotRemote",
)

ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="portalbrasil.legislativoLayer:AcceptanceTesting",
)
