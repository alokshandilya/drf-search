from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = "__all__"
        fields = [
            "title",
            "content",
            "price",
            "sale_price",  # it's a django model property
        ]
