from rest_framework import serializers

from products.models import Brand

class BrandDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "name",
            "slug",
            "logo"
        ]