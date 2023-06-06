from django.shortcuts import render
from homepage.models import Products
from carousel.models import Smartphones, Laptops, Fragrances, Skincare, Groceries, HomeDecoration
import datetime

# Create your views here.

def specific_category(request, category):
    carousel = None
    all_products = Products.objects.filter(category=category)
    print(category)
    if category == "smartphones":
        carousel = Smartphones.objects.all()
    elif category == "laptops":
        carousel = Laptops.objects.all()
    elif category == "fragrances":
        carousel = Fragrances.objects.all()
    elif category == "skincare":
        carousel = Skincare.objects.all()
    elif category == "groceries":
        carousel = Groceries.objects.all()
    elif category == "home-decoration":
        carousel = HomeDecoration.objects.all()

    data = {'products':all_products,
            'carousel':carousel,
            'date': datetime.datetime.today().year,
            "topic": category,}
    

    return render(request, "templates/category/index.html", data)
