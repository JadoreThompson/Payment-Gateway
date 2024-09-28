from invoice.models import CustomInvoiceModel

from django.shortcuts import render, redirect


def products(request):
    return render(request, 'pages/products.html')


def transactions(request):
    return render(request, 'pages/transactions.html')


def customers(request):
    return render(request, 'pages/customers.html')


def invoice(request):
    if request.user.is_authenticated:
        invoices = CustomInvoiceModel.objects.filter(user=request.user)
    else:
        return redirect('login')
    return render(request, 'pages/invoice.html',{'invoices': invoices})
