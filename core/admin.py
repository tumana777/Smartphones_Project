from django.contrib import admin
from .models import Brand, Smartphone

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'price', 'quantity', 'is_active')
