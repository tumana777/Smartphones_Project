from django.urls import path
from .views import  cart_detail, add_to_cart, update_cart

app_name = 'order'

urlpatterns = [
    path('cart_detail/', cart_detail, name='cart_detail'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('update_cart/', update_cart, name='update_cart'),
]

