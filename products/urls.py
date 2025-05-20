from django.urls import path

from products.api_endpoints import *


urlpatterns = [
    path('categorylist1/', CategoryCreateAPIView.as_view(), name="category-list"),
    path('categorycreate/', CategoryCreate.as_view(), name="category-create"),
]