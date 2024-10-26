from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CartItemForm
from .models import CartItem

@login_required(login_url='admin:login')
def cart_detail(request):

    cart_items = CartItem.objects.select_related('cart').select_related('product').filter(cart_id=request.user.cart.id)

    context = {
        'cart_items': cart_items
    }

    return render(request, 'cart.html', context)

@login_required(login_url='admin:login')
def add_to_cart(request):
    if request.method != 'POST':
        return HttpResponse(status=405)

    form = CartItemForm(request.POST, cart=request.user.cart)
    if form.is_valid():
        item = form.save(commit=False)
        item.cart_id = request.user.cart.id
        item.save()
    return redirect(request.META.get('HTTP_REFERER', ''))

@login_required(login_url='admin:login')
def update_cart(request):
    if request.method == 'POST':
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