from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=apps.get_model('accounts', 'User'))
def create_cart(sender, instance, created, **kwargs):
    logger.debug("Signal is working")
    if created:
        Cart = apps.get_model('accounts', 'Cart')  # <-- kechiktirilgan import
        Cart.objects.create(user=instance)
