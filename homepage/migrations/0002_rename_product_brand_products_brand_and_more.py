# Generated by Django 4.2 on 2023-05-01 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='product_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_discount',
            new_name='discount',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_images',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_thumbnail',
            new_name='thumbnail',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='product_title',
            new_name='title',
        ),
    ]