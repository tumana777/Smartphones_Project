from django.contrib import admin
from .models import Category, Brand, Smartphone, ProductTag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'price', 'quantity', 'is_active')
