from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('user_address/<int:user>', views.user_address, name='user_address'),
    path('user_address/add_address/<int:user>', views.add_user_address, name='add_user_address'),
    path('submit_address', views.submit_address, name='submit_address'),
    path('delete_address/<address>', views.delete_address, name='delete_address'),
    path('edit_address/<address>', views.edit_address, name='edit_address'),
]
