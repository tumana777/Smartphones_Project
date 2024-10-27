from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .forms import CartItemForm
from .models import CartItem

class CartDetailView(LoginRequiredMixin, View):
    login_url = 'admin:login'

    def get(self, request):
        cart_items = CartItem.objects.select_related('cart').select_related('product').filter(cart_id=request.user.cart.id)
        context = {
            'cart_items': cart_items
        }
        return render(request, 'cart.html', context)

class AddToCartView(LoginRequiredMixin, View):
    login_url = 'admin:login'

    def post(self, request):
        form = CartItemForm(request.POST, cart=request.user.cart)
        if form.is_valid():
            item = form.save(commit=False)
            item.cart_id = request.user.cart.id
            item.save()
        return redirect(request.META.get('HTTP_REFERER', ''))

class UpdateCartView(LoginRequiredMixin, View):
    login_url = 'admin:login'

    def post(self, request):
        cart_item_id = request.POST.get('cart_item_id')
        cart_item = get_object_or_404(CartItem, id=cart_item_id, cart=request.user.cart)

        if 'increase' in request.POST:
            if cart_item.product.quantity > cart_item.quantity:
                cart_item.quantity += 1
                cart_item.save()

        if 'decrease' in request.POST:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()

        if 'remove' in request.POST:
            cart_item.delete()

        return redirect(request.META.get('HTTP_REFERER', ''))
