from rest_framework.generics import UpdateAPIView

from products.models import Brand
from products.api_endpoints.Brand.BrandUpdate.serializers import BrandUpdateSerializers

class BrandUpdateAPIView(UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandUpdateSerializers
    lookup_field = "id"