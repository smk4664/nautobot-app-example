"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from example import models
from example.tests import fixtures


class ExampleExampleModelViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the ExampleExampleModel views."""

    model = models.ExampleExampleModel
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }

    update_data = {
        "name": "Test 2",
        "description": "Updated model",
    }

    @classmethod
    def setUpTestData(cls):
        fixtures.create_exampleexamplemodel()
