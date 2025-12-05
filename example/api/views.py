"""API views for example."""

from nautobot.apps.api import NautobotModelViewSet

from example import filters, models
from example.api import serializers


class ExampleExampleModelViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """ExampleExampleModel viewset."""

    queryset = models.ExampleExampleModel.objects.all()
    serializer_class = serializers.ExampleExampleModelSerializer
    filterset_class = filters.ExampleExampleModelFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
