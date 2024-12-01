# from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
)

# from rest_framework.response import Response
# from rest_framework.views import status
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


# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     """
#     Function-based view to handle the same request as
#     `ProductListCreateAPIView`, `ProductDetailAPIView`
#     """
#     method = request.method
#
#     if method == "GET":
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Product, pk=pk)
#             serializer = ProductSerializer(obj, many=False)
#             return Response(serializer.data)
#
#         # list view
#         qs = Product.objects.all()
#         data = ProductSerializer(qs, many=True).data
#         return Response(data)
#
#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(
#             {"invalid": "not good data"},
#             status=status.HTTP_400_BAD_REQUEST,
#         )
