from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form_view, name='form'),
    path('graph/', views.graph_view, name='graph'),
]
