from django.db import models
from autoslug import AutoSlugField

class Products(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    desc = models.TextField()
    price = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    thumbnail = models.URLField()
    images = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




