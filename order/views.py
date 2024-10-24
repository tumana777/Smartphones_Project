from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Cart, CartItem
from core.models import Smartphone

def add_to_cart(request, smartphone_pk):
    smartphone = get_object_or_404(Smartphone, id=smartphone_pk)

    if smartphone.quantity <= 0:
        messages.error(request, "Sorry, this product is out of stock.")
        return redirect('core:smartphones_list')

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=smartphone)

        if not item_created:
            if cart_item.quantity + 1 > smartphone.quantity:
                messages.error(request, "Sorry, there is not enough stock to add more of this item.")
            else:
                cart_item.quantity += 1
                cart_item.save()
        else:
            cart_item.quantity = 1
            cart_item.save()
    else:
        cart = request.session.get('cart', {})

        if str(smartphone_pk) in cart:
            if cart[str(smartphone_pk)]['quantity'] + 1 > smartphone.quantity:
                messages.error(request, "Sorry, there is not enough stock to add more of this item.")
            else:
                cart[str(smartphone_pk)]['quantity'] += 1
        else:
            cart[str(smartphone_pk)] = {
                'name': smartphone.name,
                'price': smartphone.price,
                'quantity': 1
            }

        request.session['cart'] = cart

    return redirect('core:smartphones_list')
