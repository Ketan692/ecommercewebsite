from django.db import models


class Homepage(models.Model):
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Smartphones(models.Model):
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Laptops(models.Model):
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Fragrances(models.Model):
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Skincare(models.Model):
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class Groceries(models.Model):
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


class HomeDecoration(models.Model):
    thumbnail = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
