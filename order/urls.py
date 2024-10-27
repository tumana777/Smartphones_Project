from django.urls import path
from .views import  CartDetailView, AddToCartView, UpdateCartView

app_name = 'order'

urlpatterns = [
    path('cart_detail/', CartDetailView.as_view(), name='cart_detail'),
    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('update_cart/', UpdateCartView.as_view(), name='update_cart'),
]

