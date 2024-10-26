from django import forms
from django.core.exceptions import ValidationError

from core.models import Smartphone
from .models import CartItem

from django.core.exceptions import ValidationError
from django import forms
from .models import CartItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        self.cart = kwargs.pop('cart', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        requested_quantity = cleaned_data.get('quantity')

        if not product or not requested_quantity:
            return cleaned_data

        cart_item = CartItem.objects.filter(cart=self.cart, product=product).first()

        if cart_item:
            new_quantity = cart_item.quantity + requested_quantity
            if new_quantity > product.quantity:
                raise ValidationError("Requested quantity exceeds available stock.")
            else:
                cart_item.quantity = new_quantity
                cart_item.save()
                raise ValidationError("Quantity updated in cart.")

        elif requested_quantity > product.quantity:
            raise ValidationError("Requested quantity exceeds available stock.")

        return cleaned_data
