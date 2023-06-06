from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart, CartProduct

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100, default="")
    mobile = models.IntegerField()


def get_cart_count(self):
    return CartProduct.objects.filter(cart__is_paid=False, cart__user=self)


User.add_to_class("get_cart_count", get_cart_count)
