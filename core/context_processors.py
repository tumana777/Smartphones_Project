from django.db.models import Sum
from order.models import Cart

def cart_total_quantity(request):
    total_quantity = 0

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            total_quantity = cart.cartitem_set.aggregate(total=Sum('quantity'))['total'] or 0
        except Cart.DoesNotExist:
            total_quantity = 0
    else:
        total_quantity = request.session.get('total_quantity', 0)

    return {
        'total_quantity': total_quantity
    }
