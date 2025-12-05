"""API serializers for example."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from example import models


class ExampleExampleModelSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """ExampleExampleModel Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.ExampleExampleModel
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
