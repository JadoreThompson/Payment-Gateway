from django.urls import path
from . import views

urlpatterns = [
    path('create', views.ProductCreateView, name='create_product')
]
