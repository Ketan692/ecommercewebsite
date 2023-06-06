from django.contrib import admin
from cart.models import Cart, CartProduct, Coupon

class CartAdmin(admin.ModelAdmin):
    list_display = ("user", "is_paid",)

class CartProductAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity")
    
class CouponAdmin(admin.ModelAdmin):
    list_display = ("code", "discount", "minimum")

admin.site.register(Cart, CartAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Coupon, CouponAdmin)
