from rest_framework.generics import ListAPIView

from products.models import ProductVariant

from products.api_endpoints.ProductVariant.ProductList.serializers import ProductVariantListSerializer

class ProductVariantListAPiView(ListAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer
    permission_classes = []