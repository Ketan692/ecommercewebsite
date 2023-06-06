from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
from homepage.models import Products
import datetime
from carousel.models import Homepage
from category.models import Category

def home(request):
    # data = {'products' : response}
    
    #below code is just to add json products to our database
    # response = requests.get(url="https://dummyjson.com/products").json()['products']
    # for i in response:
    #     title = i['title']
    #     desc = i['description']
    #     price = int(i['price'])
    #     discount = i['discountPercentage']
    #     rating = i['rating']
    #     stock = i['stock']
    #     brand = i['brand']
    #     category = i['category']
    #     thumbnail = i['thumbnail']
    #     images = i['images']
    #     # print(type(title), type(desc), type(price), type(discount), type(rating), type(stock), type(brand), type(category), type(thumbanail), type(images), sep="\n")
    #     # print(title, desc, price, discount, rating, stock, brand, category, thumbanail, images, sep="\n")
    #     new_record = Products(title=title, desc=desc, price=price, discount=discount, rating=rating, stock=stock, brand=brand, category=category, thumbnail=thumbnail, images=images)
    #     new_record.save()
    all_products = Products.objects.all()
    carousel = Homepage.objects.all()
    categories = Category.objects.all()

    data = {'products':all_products,
            'carousel':carousel,
            'categories': categories,
            'date': datetime.datetime.today().year,}
    

    return render(request, "templates/homepage/index.html", data)


def specific_product(request, slug):
    product = Products.objects.filter(slug=slug)[0]
    product_images = [i[1:-1] for i in product.images[1:-1].split(", ")][:-1]
    data = {
        "product": product,
        "product_images": product_images
    }
    return render(request, "templates/homepage/specific_product.html", data)
