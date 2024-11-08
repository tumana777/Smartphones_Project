# Generated by Django 5.1.2 on 2024-11-08 08:41

import autoslug.fields
import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_remove_category_slug_en_remove_category_slug_ka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ka',
            field=models.CharField(max_length=20, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='core.category', verbose_name='Parent'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', verbose_name='Slug'),
        ),
    ]
