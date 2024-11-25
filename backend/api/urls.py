from django.urls import path

from .views import ProductDetailAPIView, api_home

urlpatterns = [
    path("", api_home),
    path("products/<int:pk>/", ProductDetailAPIView.as_view()),
]
