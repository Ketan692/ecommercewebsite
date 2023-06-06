from django.urls import path
from category import views

urlpatterns = [
    path('<category>', views.specific_category, name="specific_category"),
]