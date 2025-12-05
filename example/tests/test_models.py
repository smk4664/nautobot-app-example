"""Test ExampleExampleModel."""

from nautobot.apps.testing import ModelTestCases

from example import models
from example.tests import fixtures


class TestExampleExampleModel(ModelTestCases.BaseModelTestCase):
    """Test ExampleExampleModel."""

    model = models.ExampleExampleModel

    @classmethod
    def setUpTestData(cls):
        """Create test data for ExampleExampleModel Model."""
        super().setUpTestData()
        # Create 3 objects for the model test cases.
        fixtures.create_exampleexamplemodel()

    def test_create_exampleexamplemodel_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        exampleexamplemodel = models.ExampleExampleModel.objects.create(name="Development")
        self.assertEqual(exampleexamplemodel.name, "Development")
        self.assertEqual(exampleexamplemodel.description, "")
        self.assertEqual(str(exampleexamplemodel), "Development")

    def test_create_exampleexamplemodel_all_fields_success(self):
        """Create ExampleExampleModel with all fields."""
        exampleexamplemodel = models.ExampleExampleModel.objects.create(name="Development", description="Development Test")
        self.assertEqual(exampleexamplemodel.name, "Development")
        self.assertEqual(exampleexamplemodel.description, "Development Test")
