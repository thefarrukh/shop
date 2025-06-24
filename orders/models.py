from django.db import models

from common.models import BaseModel
from common.choices import OrderStatus
from django.utils.translation import gettext_lazy as _


class Order(BaseModel):
    user = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.BigIntegerField(null=False, blank=False)
    status = models.CharField(choices=OrderStatus.choices, null=False, blank=False)
    notes = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Order({self.id})"
    
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Order")


class OrderItem(BaseModel):
    order = models.ForeignKey('orders.Order', on_delete=models.RESTRICT, null=True, blank=True)
    product = models.ForeignKey('products.ProductVariant', on_delete=models.RESTRICT, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return f"Order({self.id})"
    
    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Item")