import json

# Dir
from invoice.models import CustomInvoiceModel
from transactions.models import CustomTransactionsModel

# FastAPI
from django.shortcuts import render
from django.http import JsonResponse


def receive_invoice_updates(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        invoice = CustomInvoiceModel.objects.filter(invoice_id=body['data']['invoice_id'])

        if invoice:
            if body['type'] == 'invoice.deleted':
                invoice.delete()
            elif body['type'] == 'invoice.paid':
                invoice.status = 'paid'
                invoice.save()
            else:
                return JsonResponse(status=408, data={"message": "Invoice wasn't deleted or paid"})
            return JsonResponse({"message": "Success"}, status=200)
        return JsonResponse(status=400, data={'message': 'No such invoice'})


def receive_transaction_updates(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        transaction = CustomTransactionsModel.objects.filter(transaction_id=body['data']['transaction_id'])

        if transaction:
            return JsonResponse(status=409, data={"message": "Transaction already exists"})
        else:
            # return 10
            return JsonResponse(status=200, data={"message": "Transaction doesn't exist"})

        # # else:
        # #     CustomTransactionsModel.objects.create()
