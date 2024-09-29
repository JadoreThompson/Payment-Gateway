from invoice.models import CustomInvoiceModel

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


@login_required
def products(request):
    return render(request, 'pages/products.html')

@login_required
def transactions(request):
    return render(request, 'pages/transactions.html')


@login_required
def customers(request):
    return render(request, 'pages/customers.html')


@login_required
def invoice(request):
    if request.user.is_authenticated:
        invoices = CustomInvoiceModel.objects.filter(user=request.user)
    else:
        return redirect('login')
    return render(request, 'pages/invoice.html',{'invoices': invoices})
