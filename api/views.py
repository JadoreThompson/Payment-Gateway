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
        invoice_id = body['data']['invoice_id']
        invoice = CustomInvoiceModel.objects.get(invoice_id=invoice_id)

        if invoice:
            print(invoice.invoice_id)
            print(invoice.status)

            if body['type'] == 'invoice.deleted':
                invoice.delete()
                return JsonResponse(status=200, data={"message": "Invoice deleted"})
            elif body['type'] == 'invoice.paid':
                invoice.status = 'paid'
                invoice.save()
                return JsonResponse(status=200, data={"message": "Invoice status updated to paid"})
            else:
                return JsonResponse(status=408, data={"message": "Invoice wasn't deleted or paid"})
        return JsonResponse(status=400, data={'message': 'No such invoice'})


def receive_transaction_updates(request):
    if request.method == 'POST':
        print('Got invoice update')
        body = json.loads(request.body)
        transaction = CustomTransactionsModel.objects.filter(transaction_id=body['data']['transaction_id'])

        if transaction:
            return JsonResponse(status=409, data={"message": "Transaction already exists"})
        else:
            return JsonResponse(status=200, data={"message": "Transaction doesn't exist"})
