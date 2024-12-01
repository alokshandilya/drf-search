from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(RetrieveAPIView):
    """
    RetrieveAPIView:

    Used for read-only endpoints to represent a single model instance.
    Provides a `get` method handler.
    Extends: `GenericAPIView`, `RetrieveModelMixin`
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"  # default


class ProductListCreateAPIView(ListCreateAPIView):
    """
    ListCreateAPIView:

    Used for read-write endpoints to represent a collection of model instances.
    Provides `get` and `post` method handlers.
    Extends: `GenericAPIView`, `ListModelMixin`, `CreateModelMixin`
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UpdateAPIView):
    """
    Used for update-only endpoints for a single model instance.

    Provides put and patch method handlers.
    Extends: GenericAPIView, UpdateModelMixin
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"
