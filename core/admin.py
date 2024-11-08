from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Category, Brand, Smartphone, ProductTag

@admin.register(Category)
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ('name',)

@admin.register(Brand)
class BrandAdmin(TabbedTranslationAdmin):
    list_display = ('name',)

@admin.register(ProductTag)
class ProductTagAdmin(TabbedTranslationAdmin):
    list_display = ('name',)

@admin.register(Smartphone)
class SmartphoneAdmin(TabbedTranslationAdmin):
    list_display = ('brand', 'name', 'price', 'quantity', 'is_active')
