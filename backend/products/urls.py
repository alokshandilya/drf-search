from django.urls import path

from .views import (
    ProductCreateAPIView,
    ProductDetailAPIView,
    ProductListAPIView,
)

urlpatterns = [
    path("", ProductListAPIView.as_view()),
    path("create/", ProductCreateAPIView.as_view()),
    path("<int:pk>/", ProductDetailAPIView.as_view()),
]
