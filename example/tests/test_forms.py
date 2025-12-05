"""Test exampleexamplemodel forms."""

from django.test import TestCase

from example import forms


class ExampleExampleModelTest(TestCase):
    """Test ExampleExampleModel forms."""

    def test_specifying_all_fields_success(self):
        form = forms.ExampleExampleModelForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.ExampleExampleModelForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_exampleexamplemodel_is_required(self):
        form = forms.ExampleExampleModelForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
