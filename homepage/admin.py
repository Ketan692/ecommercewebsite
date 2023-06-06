from django.contrib import admin
from homepage.models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("title", "desc", "price", "discount", "rating", "stock", "brand", "category", "thumbnail", "images")

admin.site.register(Products, ProductsAdmin)
# Register your models here.
