from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner_msg = serializers.SerializerMethodField()

    class Meta:
        model = Product
        # fields = "__all__"
        fields = [
            "title",
            "content",
            "price",
            "sale_price",  # it's a django model property
            "owner_msg",  # it's an instance method
        ]

    def get_owner_msg(self, obj):
        # obj is the instance of the model

        # print(obj)
        # print(obj.id)
        # print(obj.title)
        # print(obj.price)
        # print(obj.sale_price)
        # print(obj.get_discount())

        return obj.get_owner_msg()
