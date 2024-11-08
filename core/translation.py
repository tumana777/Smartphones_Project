from modeltranslation.translator import register, TranslationOptions
from .models import Category, Brand, ProductTag, Smartphone

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Brand)
class BrandTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ProductTag)
class ProductTagTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Smartphone)
class SmartphoneTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)