# Generated by Django 4.2 on 2023-05-01 17:51

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_rename_product_brand_products_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
