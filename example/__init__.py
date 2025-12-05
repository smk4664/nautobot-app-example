"""App declaration for example."""

# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

from nautobot.apps import NautobotAppConfig

__version__ = metadata.version(__name__)


class ExampleConfig(NautobotAppConfig):
    """App configuration for the example app."""

    name = "example"
    verbose_name = "Example"
    version = __version__
    author = "Network to Code, LLC"
    description = "Example."
    base_url = "example"
    required_settings = []
    default_settings = {}
    docs_view_name = "plugins:example:docs"
    searchable_models = ["exampleexamplemodel"]


config = ExampleConfig  # pylint:disable=invalid-name
