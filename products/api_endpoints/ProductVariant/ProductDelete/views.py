from rest_framework.generics import DestroyAPIView

from products.models import ProductVariant
from products.api_endpoints.ProductVariant.ProductDelete.serializers import ProductDeleteSerializers

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductDeleteSerializers
    lookup_field = "id"