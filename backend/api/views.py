from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.order_by("?").first()
    data = {}

    if instance:
        data = ProductSerializer(instance).data

    return Response(data)
