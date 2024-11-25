from rest_framework.generics import RetrieveAPIView

from .models import Product
from .serializers import ProductSerializer

# Create your views here.


class ProductDetailAPIView(RetrieveAPIView):
    """
    Used for read-only endpoints to represent a single model instance.
    Provides a `get` method handler.
    Extends: `GenericAPIView`, `RetrieveModelMixin`
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"  # default
