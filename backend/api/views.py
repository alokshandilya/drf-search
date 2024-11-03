from django.forms.models import model_to_dict
from django.http import JsonResponse
from products.models import Product


def api_home(request, *args, **kwargs):
    random_product = Product.objects.order_by("?").first()
    data = {}

    if random_product:
        data = model_to_dict(random_product, fields=["id", "title", "price"])

    return JsonResponse(data)
