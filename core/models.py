from django.db import models
from autoslug import AutoSlugField


class Brand(models.Model):
    name = models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

class Smartphone(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='smartphones')
    name = models.CharField(max_length=20)
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