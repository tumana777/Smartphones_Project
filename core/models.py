from django.db import models
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _


class Category(MPTTModel):
    name = models.CharField(max_length=20, unique=True, verbose_name=_('Name'))
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children', verbose_name=_('Parent'))
    slug = AutoSlugField(populate_from='name', verbose_name=_('Slug'))

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'category'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        if self.parent:
            return f"{self.parent} -> {self.name}"
        else:
            return self.name

class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=_("name"))
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name=_("slug"))

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=_("name"))

    class Meta:
        db_table = _('product_tag')
        verbose_name_plural = _("product_tags")

    def __str__(self):
        return self.name

class Smartphone(models.Model):
    category = models.ManyToManyField('Category', related_name='smartphones', verbose_name=_("category"))
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='smartphones', verbose_name=_("brand"))
    tags = models.ManyToManyField('ProductTag', related_name='smartphones', verbose_name=_("tags"))
    name = models.CharField(max_length=50, verbose_name=_("name"))
    price = models.IntegerField(verbose_name=_("price"))
    quantity = models.IntegerField(verbose_name=_("quantity"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))
    description = models.TextField(null=True, blank=True, verbose_name=_("description"))
    created_at = models.DateField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("updated at"))
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=_("image"))
    imageUrl = models.URLField(null=True, blank=True, verbose_name=_("image url"))
    slug = AutoSlugField(populate_from='name', unique=True, verbose_name=_("slug"))

    def __str__(self):
        return self.name