from . import views

from django.urls import path
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('receive-invoice-updates', csrf_exempt(views.receive_invoice_updates), name='receive_invoice_updates'),
    path('receive-transaction-updates', csrf_exempt(views.receive_transaction_updates), name='receive_transaction_updates')
]
