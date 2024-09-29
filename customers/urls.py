from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('create', csrf_exempt(CreateCustomerView.as_view()), name='create_customer')
]
