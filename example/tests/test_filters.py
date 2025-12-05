"""Test ExampleExampleModel Filter."""

from nautobot.apps.testing import FilterTestCases

from example import filters, models
from example.tests import fixtures


class ExampleExampleModelFilterTestCase(FilterTestCases.FilterTestCase):
    """ExampleExampleModel Filter Test Case."""

    queryset = models.ExampleExampleModel.objects.all()
    filterset = filters.ExampleExampleModelFilterSet
    generic_filter_tests = (
        ("id",),
        ("created",),
        ("last_updated",),
        ("name",),
    )

    @classmethod
    def setUpTestData(cls):
        """Setup test data for ExampleExampleModel Model."""
        fixtures.create_exampleexamplemodel()

    def test_q_search_name(self):
        """Test using Q search with name of ExampleExampleModel."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for ExampleExampleModel."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
