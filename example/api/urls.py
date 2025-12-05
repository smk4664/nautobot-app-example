"""Django API urlpatterns declaration for example app."""

from nautobot.apps.api import OrderedDefaultRouter

from example.api import views

router = OrderedDefaultRouter()
# add the name of your api endpoint, usually hyphenated model name in plural, e.g. "my-model-classes"
router.register("example-example-models", views.ExampleExampleModelViewSet)

app_name = "example-api"
urlpatterns = router.urls
