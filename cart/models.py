from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
from homepage.models import Products


# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=15)
    discount = models.IntegerField(blank=True, null=True)
    minimum = models.IntegerField(blank=True, null=True)


class Cart(models.Model):
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)


class CartProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)



