# Directory Modules
from invoice.models import CustomInvoiceModel
from customers.models import CustomCustomerModel
from transactions.models import CustomTransactionsModel
from products.models import CustomProductsModel

# Django Modules
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def products(request):
    products = CustomProductsModel.objects.filter(user=request.user)
    return render(request, 'pages/products.html', {"products": products})


@login_required
def transactions(request):
    transactions = CustomTransactionsModel.objects.filter(user=request.user)
    return render(request, 'pages/transactions.html', {'transactions': transactions})


@login_required
def customers(request):
    customers = CustomCustomerModel.objects.filter(user=request.user)
    return render(request, 'pages/customers.html', {'customers': customers})


@login_required
def invoice(request):
    invoices = CustomInvoiceModel.objects.filter(user=request.user)
    if request.GET.get('status'):
        invoices = invoices.filter(status=request.GET.get('status'))
    return render(request, 'pages/invoice.html', {'invoices': invoices})
