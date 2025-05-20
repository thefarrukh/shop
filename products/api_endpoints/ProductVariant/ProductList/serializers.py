from rest_framework import serializers

from products.models import ProductVariant

class ProductVariantListSerializer(serializers.ModelSerializer):
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
        
    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.name,
            "price": instance.price,
            "product": instance.product,
            "images": instance.images,
            "stock": instance.stock,
            "color": instance.color,
            "size": instance.size,
            "stock": instance.stock,
            "is_active": instance.is_active
        }

        return instance 