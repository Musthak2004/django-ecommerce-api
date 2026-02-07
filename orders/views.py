from django.views.generic import ListView, DetailView
from .models import Order

class OrderListView(ListView):
    model = Order
    template_name = "order_list.html"
    context_object_name = "orders"

class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"
    context_object_name = "order"

    def get_queryset(self):
        # security: user oda orders mattum
        return Order.objects.filter(user=self.request.user)