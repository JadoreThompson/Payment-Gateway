from django.urls import path
from . import views

urlpatterns = [
    path('create', views.ProductCreateView.as_view(), name='create_product')
]
