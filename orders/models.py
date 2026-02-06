from django.db import models
from accounts.models import User
from store.models import Product
from django.urls import reverse


class Order(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"

    def get_absolute_url(self):
        return reverse("order_detail", args=[self.id])

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
