from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<slug>', views.specific_product, name="specific_product")
]