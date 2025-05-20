from rest_framework import serializers

from products.models import Product

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "brand",
            "slug",
            "default_images",
            "is_active",
            "category"
        ]

    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.name,
            "brand": instance.brand,
            "slug": instance.slug,
            "default_images": instance.default_images,
            "is_active": instance.is_active,
            "category": instance.category
        }

        return instance