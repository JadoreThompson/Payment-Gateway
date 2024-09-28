from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views


urlpatterns = [
    path('create', views.CreateInvoiceView.as_view(), name='create_invoice'),
]
