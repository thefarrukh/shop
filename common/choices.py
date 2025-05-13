from django.db.models import TextChoices


class OrderStatus(TextChoices):
    PENDING = 'PENDING', 'PENDING'
    DELIVERED = 'DELEVERED', 'DELEVERED'
    CANCELLED = 'CANCELLED', 'CANCELLED'