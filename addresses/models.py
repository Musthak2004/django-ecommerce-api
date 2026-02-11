from django.db import models
from django.conf import settings
from django.urls import reverse

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="addresses")
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_cpde = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    address_type = models.CharField(
        max_length=10,
        choices=[("shipping", "Shipping"), ("billing", "Billing")],
        default="shipping"
    )

    def __str__(self):
        return f"{self.full_name} - {self.city}, {self.country}"
    
    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})
    
