from django.urls import path

from .views import (
    ProductDetailAPIView,
    ProductListCreateAPIView,
    # product_alt_view,
)

urlpatterns = [
    path("", ProductListCreateAPIView.as_view()),
    # path("", product_alt_view),
    path("<int:pk>/", ProductDetailAPIView.as_view()),
    # path("<int:pk>/", product_alt_view),
]
