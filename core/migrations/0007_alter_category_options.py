# Generated by Django 5.1.2 on 2024-11-08 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_category_name_en_category_name_ka_category_slug_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'category'},
        ),
    ]
