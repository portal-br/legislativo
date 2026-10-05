from . import TYPES_WITH_DEFAULT_WORKFLOW
from . import TYPES_WITHOUT_WORKFLOW
from . import WORKFLOW_ID
from Products.CMFPlone.WorkflowTool import WorkflowTool

import pytest


class TestWorkflow:
    @pytest.fixture(autouse=True)
    def _setup(self, portal) -> None:
        """Bind the workflow tool to the test instance."""
        self.wf_tool: WorkflowTool = portal.portal_workflow

    def test_default_chain(self):
        """The default chain is the copied simple_publication_workflow."""
        assert self.wf_tool.getDefaultChain() == (WORKFLOW_ID,)

    @pytest.mark.parametrize("portal_type", TYPES_WITH_DEFAULT_WORKFLOW)
    def test_chain_default_types(self, portal_type: str):
        """Content types use the default chain."""
        assert self.wf_tool.getChainForPortalType(portal_type) == (WORKFLOW_ID,)

    @pytest.mark.parametrize("portal_type", TYPES_WITHOUT_WORKFLOW)
    def test_chain_without_workflow(self, portal_type: str):
        """Files, images and the site itself have no workflow."""
        assert self.wf_tool.getChainForPortalType(portal_type) == ()

    def test_initial_state(self, plone_definition):
        """The initial state matches the Plone definition."""
        workflow = self.wf_tool[WORKFLOW_ID]
        assert workflow.initial_state == plone_definition.get("initial_state")

    def test_states(self, plone_definition):
        """The states match the Plone definition."""
        expected = sorted(s.get("state_id") for s in plone_definition.iter("state"))
        workflow = self.wf_tool[WORKFLOW_ID]
        assert sorted(workflow.states.objectIds()) == expected

    def test_transitions(self, plone_definition):
        """The transitions match the Plone definition."""
        expected = sorted(
            t.get("transition_id") for t in plone_definition.iter("transition")
        )
        workflow = self.wf_tool[WORKFLOW_ID]
        assert sorted(workflow.transitions.objectIds()) == expected
