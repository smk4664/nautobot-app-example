"""Views for example."""

from nautobot.apps.views import NautobotUIViewSet
from nautobot.apps.ui import ObjectDetailContent, ObjectFieldsPanel, ObjectsTablePanel, SectionChoices
from nautobot.core.templatetags import helpers

from example import filters, forms, models, tables
from example.api import serializers


class ExampleExampleModelUIViewSet(NautobotUIViewSet):
    """ViewSet for ExampleExampleModel views."""

    bulk_update_form_class = forms.ExampleExampleModelBulkEditForm
    filterset_class = filters.ExampleExampleModelFilterSet
    filterset_form_class = forms.ExampleExampleModelFilterForm
    form_class = forms.ExampleExampleModelForm
    lookup_field = "pk"
    queryset = models.ExampleExampleModel.objects.all()
    serializer_class = serializers.ExampleExampleModelSerializer
    table_class = tables.ExampleExampleModelTable

    # Here is an example of using the UI  Component Framework for the detail view.
    # More information can be found in the Nautobot documentation:
    # https://docs.nautobot.com/projects/core/en/stable/development/core/ui-component-framework/
    object_detail_content = ObjectDetailContent(
        panels=[
            ObjectFieldsPanel(
                weight=100,
                section=SectionChoices.LEFT_HALF,
                fields="__all__",
                # Alternatively, you can specify a list of field names:
                # fields=[
                #     "name",
                #     "description",
                # ],
                # Some fields may require additional configuration, we can use value_transforms
                # value_transforms={
                #     "name": [helpers.bettertitle]
                # },
            ),
            # If there is a ForeignKey or M2M with this model we can use ObjectsTablePanel
            # to display them in a table format.
            # ObjectsTablePanel(
                # weight=200,
                # section=SectionChoices.RIGHT_HALF,
                # table_class=tables.ExampleExampleModelTable,
                # You will want to filter the table using the related_name
                # filter="exampleexamplemodels",
            # ),
        ],
    )
