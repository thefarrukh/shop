from rest_framework.generics import DestroyAPIView

from products.models import Brand
from products.api_endpoints.Brand.BrandDelete.serializers import BrandDeleteSerializer

class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDeleteSerializer
    lookup_field = "id"