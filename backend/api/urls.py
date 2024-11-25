from django.urls import include, path

from .views import (
    api_home,
)

urlpatterns = [
    path("", api_home),
    path("products/", include("products.urls")),
]
