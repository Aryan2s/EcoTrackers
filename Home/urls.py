from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
        path("", views.index, name='Home'),
        path("about", views.About, name='About'),
        path("services", views.Services, name='Services'),
        path("contact", views.Contact_page, name='Contact'),
        path('upload/',views.upload_image_with_location,name='Upload'),
        path('shop/',views.shopping,name='shop'),
    ]
        