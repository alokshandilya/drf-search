from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    random_product = Product.objects.order_by("?").first()
    data = {}

    if random_product:
        data = model_to_dict(
            random_product,
            fields=[
                "id",
                "title",
                "price",
                "sale_price",  # model_to_dict doesn't show property
            ],
        )

    return Response(data)
