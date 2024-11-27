from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
)

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


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


class ProductCreateAPIView(CreateAPIView):
    """
    CreateAPIView:

    Used for create-only endpoints for a single model instance.
    Provides a `post` method handler.
    Extends: `GenericAPIView`, `CreateModelMixin`
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    """
    ListAPIView:

    Used for read-only endpoints to represent a collection of model instances.
    Provides a `get` method handler.
    Extends: `GenericAPIView`, `ListModelMixin`
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
