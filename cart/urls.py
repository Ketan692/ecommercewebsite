from django.urls import path
from cart import views

urlpatterns = [
    path('add-to-cart/<slug>', views.add_to_cart, name='add_to_cart'),
    path('user/cart', views.cart, name='cart'),
    path('user/cart/apply_coupon', views.apply_coupon, name='apply_coupon'),
    path('user/cart/delete_coupon', views.delete_coupon, name='delete_coupon'),
    path('user/cart/delete_item/<id>', views.delete_item, name='delete_item'),
    path('user/cart/adjust_quantity/<id>/<process>', views.adjust_quantity, name='adjust_quantity'),
]