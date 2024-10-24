# Generated by Django 5.1.2 on 2024-10-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_category_name_alter_smartphone_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Product Tags',
                'db_table': 'Product Tag',
            },
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='smartphone',
            name='tags',
            field=models.ManyToManyField(related_name='smartphones', to='core.producttag'),
        ),
    ]