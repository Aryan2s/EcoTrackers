from django.urls import path
from . import views

urlpatterns = [
    path('register',views.register, name='register'),       
    path('login/',views.LoginPage,name='login'),
    path('Logout/',views.Logout,name='Logout'),
]
