from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "created_at", "total")
    list_filter = ("status", "created_at")
    search_fields = ("user__email",)
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "price", "quantity", "get_total")
    list_filter = ("order",)
    search_fields = ("product__name", "order__user__email")

    def get_total(self, obj):
        return obj.get_total_price()

    get_total.short_description = "Total Price"
