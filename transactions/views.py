from django.shortcuts import render
from django.views import View


class TransactionView(View):
    def get(self, request):
        return render(request, 'transactions/transactions.html')
