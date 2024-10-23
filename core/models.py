from django.db import models
from autoslug import AutoSlugField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=20, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    slug = AutoSlugField(populate_from='name')

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
    name = models.CharField(max_length=20, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

class ProductTag(models.Model):
    name = models.CharField(max_length=10, unique=True)

    class Meta:
        db_table = 'Product Tag'
        verbose_name_plural = 'Product Tags'

    def __str__(self):
        return self.name

class Smartphone(models.Model):
    category = models.ManyToManyField('Category', related_name='smartphones')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='smartphones')
    tags = models.ManyToManyField('ProductTag', related_name='smartphones')
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    imageUrl = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name