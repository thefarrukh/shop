from rest_framework.generics import RetrieveAPIView

from products.models import ProductVariant
from products.api_endpoints.ProductVariant.ProductRetrieve.serializers import ProductVariantSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = []