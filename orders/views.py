from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .models import Order, OrderItem
from store.models import Product

@method_decorator(login_required, name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = "order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')



@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"
    context_object_name = "order"

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)



@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    order, created = Order.objects.get_or_create(
        user=request.user,
        status="pending"
    )

    # Get existing OrderItem or create
    order_item, created_item = OrderItem.objects.get_or_create(
        order=order,
        product=product,
        defaults={'price': product.price, 'quantity': 1}
    )

    if not created_item:
        order_item.quantity += 1
        order_item.save()

    return redirect('order_detail', pk=order.id)
