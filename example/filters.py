"""Filtering for example."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from example import models


class ExampleExampleModelFilterSet(NameSearchFilterSet, NautobotFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for ExampleExampleModel."""

    class Meta:
        """Meta attributes for filter."""

        model = models.ExampleExampleModel

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
