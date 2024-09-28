from django.shortcuts import render


def products(request):
    return render(request, 'pages/products.html')


def transactions(request):
    return render(request, 'pages/transactions.html')


def customers(request):
    return render(request, 'pages/customers.html')


def invoices(request):
    return render(request, 'pages/invoices.html')
