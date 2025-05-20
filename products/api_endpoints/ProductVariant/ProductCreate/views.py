from rest_framework.generics import CreateAPIView
from products.api_endpoints.ProductVariant.ProductCreate.serializers import ProductVariantSerializer
from products.models import ProductVariant

class ProductCreateAPIView(CreateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer