from rest_framework import serializers

from products.models import ProductVariant

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = [
            "name",
            "price",
            "product",
            "images",
            "stock",
            "color",
            "size",
            "stock",
            "is_active"
        ]