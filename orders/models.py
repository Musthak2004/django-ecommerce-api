from django.db import models
from accounts.models import User
from django.urls import reverse
from decimal import Decimal
from store.models import Product


class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    shipping_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    discount_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    @property
    def subtotal(self):
        return sum(
            item.get_total_price()
            for item in self.items.all()
    )

    @property
    def total(self):
        return self.subtotal + self.shipping_amount - self.discount_amount

    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"

    def get_absolute_url(self):
        return reverse("order_detail", args=[self.id])

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("order", "product")

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_total_price(self):
        return self.price * self.quantity

    