from django.urls import path

from .views import (
    ProductDetailAPIView,
)

urlpatterns = [
    path("<int:pk>/", ProductDetailAPIView.as_view()),
]
