from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def api_home(request, *args, **kwargs):
    if request.method == "GET":
        instance = Product.objects.order_by("?").first()
        data = {}

        if instance:
            data = ProductSerializer(instance).data

        return Response(data)

    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
