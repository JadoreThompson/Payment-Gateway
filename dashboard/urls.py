from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products, name='products'),
    path('customers', views.customers, name='customers'),
    path('transactions', views.transactions, name='transactions'),
    path('invoices', views.invoices, name='invoices')
]
