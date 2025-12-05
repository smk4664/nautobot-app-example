"""Forms for example."""

from django import forms
from nautobot.apps.constants import CHARFIELD_MAX_LENGTH
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from example import models


class ExampleExampleModelForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """ExampleExampleModel creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.ExampleExampleModel
        fields = "__all__"


class ExampleExampleModelBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """ExampleExampleModel bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.ExampleExampleModel.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False, max_length=CHARFIELD_MAX_LENGTH)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class ExampleExampleModelFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.ExampleExampleModel
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name.",
    )
    name = forms.CharField(required=False, label="Name")
