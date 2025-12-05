"""Create fixtures for tests."""

from example.models import ExampleExampleModel


def create_exampleexamplemodel():
    """Fixture to create necessary number of ExampleExampleModel for tests."""
    ExampleExampleModel.objects.create(name="Test One")
    ExampleExampleModel.objects.create(name="Test Two")
    ExampleExampleModel.objects.create(name="Test Three")
