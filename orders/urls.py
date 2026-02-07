from django.urls import path
from .views import OrderListView, OrderDetailView, add_to_cart

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path("<int:pk>/", OrderDetailView.as_view(), name="order_detail"),
    path("add-to-cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
]
