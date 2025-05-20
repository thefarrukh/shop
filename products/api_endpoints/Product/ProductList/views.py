from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
)
from rest_framework.response import Response

from products.models import Product
from products.api_endpoints.Product.ProductList.serializers import ProductListSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer
    permission_classes = []