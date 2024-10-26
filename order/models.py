from django.db import models

class Cart(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s cart"

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('core.Smartphone', on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product} - {self.quantity}"

    def total(self):
        return self.quantity * self.product.price