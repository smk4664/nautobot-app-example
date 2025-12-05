"""Django urlpatterns declaration for example app."""

from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView
from nautobot.apps.urls import NautobotUIViewSetRouter


from example import views


app_name = "example"
router = NautobotUIViewSetRouter()

# The standard is for the route to be the hyphenated version of the model class name plural.
# for example, ExampleModel would be example-models.
router.register("example-example-models", views.ExampleExampleModelUIViewSet)


urlpatterns = [
    path("docs/", RedirectView.as_view(url=static("example/docs/index.html")), name="docs"),
]

urlpatterns += router.urls
