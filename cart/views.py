from django.shortcuts import render, redirect
from homepage.models import Products
from django.contrib.auth.models import User
from cart.models import Cart, CartProduct, Coupon
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def add_to_cart(request, slug):
    user = request.user
    product = Products.objects.filter(slug=slug)[0]
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)
    prod_exist = cart_product = CartProduct.objects.filter(cart=cart, product=product,)

    if prod_exist:
        prod_exist[0].quantity += 1
        prod_exist[0].save()
        prod_exist[0].total = prod_exist[0].product.price * prod_exist[0].quantity
        prod_exist[0].save()
    else:
        cart_product = CartProduct.objects.create(cart=cart, product=product, quantity=1, total=product.price)
        cart_product.save()
    return redirect("home")

def cart(request):
    the_cart = Cart.objects.get(is_paid=False, user=request.user)
    cart_products = CartProduct.objects.filter(cart=the_cart)
    total_price = 0
    total_quantity = 0
    for i in cart_products:
        total_price += i.quantity*i.product.price
        total_quantity += i.quantity

    if the_cart.coupon:
        total_price -= the_cart.coupon.discount
    
    data = {
        "main_cart":the_cart,
        "cart":cart_products,
        "cart_total":total_price,
        "total_quantity":total_quantity,
    }
    return render(request, "templates/cart/index.html", data)


def apply_coupon(request):
    if request.method == "POST":
        the_cart = Cart.objects.get(is_paid=False, user=request.user)
        coupon_code = request.POST.get('coupon_code')
        is_valid_code = Coupon.objects.filter(code=coupon_code)[0]
        cart_products = CartProduct.objects.filter(cart=the_cart)
        total_price = 0
        for i in cart_products:
            total_price += i.quantity*i.product.price

        if not is_valid_code:
            messages.error(request, "invalid coupon")
        elif total_price < is_valid_code.minimum:
            messages.warning(request, f"cart value must be at least ${is_valid_code.minimum}")
        elif is_valid_code:
            the_cart.coupon = is_valid_code
            the_cart.save()
            messages.success(request, f"{is_valid_code.code} applied successfully :)")


        return redirect("cart")
    return redirect("cart")


def delete_coupon(request):
    the_cart = Cart.objects.get(is_paid=False, user=request.user)
    the_cart.coupon = None
    the_cart.save()
    return redirect("cart")


def adjust_quantity(request, id, process):
    the_product = CartProduct.objects.filter(id=id)[0]
    if process=="plus":
        the_product.quantity += 1
        the_product.total += the_product.product.price
        the_product.save()
    elif process=="minus":
        if the_product.quantity == 1:
            return redirect("delete_item", id=id)
        else:
           the_product.quantity -= 1
           the_product.total -= the_product.product.price
           the_product.save()
    return redirect("cart")


def delete_item(request, id):
    the_product = CartProduct.objects.filter(id=id)
    the_product.delete()
    return redirect("cart")

