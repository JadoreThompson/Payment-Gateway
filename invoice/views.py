import json
import requests
import aiohttp

from tools import STRIPE_MICROSERVICE
from invoice.models import CustomInvoiceModel

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View


class CreateInvoiceView(View):
    def get(self, request):
        return render(request, 'invoice/create_invoice.html')

    def post(self, request):
        """
        :param request:
        :return: Created invoice
        """
        try:
            data = request.POST.dict()
            post_data = {
                "new_product": {
                    "name": data['product_name']
                },
                'new_customer': {
                    'name': data['customer_name'],
                    'email': data['customer_email'],
                    'description': data['description']
                },
                'unit_amount': int(data['unit_amount']) * 100,
                'currency': data['currency'],
                'due_date': data['due_date'],
                'draft': data['draft']
            }

            # Sending to Microservice
            rsp = requests.post(f"{STRIPE_MICROSERVICE}/payments/invoice/create", json=post_data)
            rsp_data = rsp.json()

            # Handling response
            if rsp.status_code == 500:
                messages.error(request, rsp_data['message'])
                return render(request, 'invoice/create_invoice.html')

            if rsp.status_code == 200:
                invoice_data = {
                    'invoice_id': rsp_data['invoice']['invoice'], 'amount': int(rsp_data['invoice']['amount']),
                    'customer_name': data['customer_name'], 'customer_email': data['customer_email'],
                }
                CustomInvoiceModel.objects.create(user=request.user, **invoice_data)
                messages.success(request, 'Successfully created Invoice')
                return redirect('invoice')

            if rsp.status_code == 422:
                raise Exception
        except json.JSONDecodeError as e:
            messages.error(request, 'Internal server error')
            return render(request, 'invoice/create_invoice.html', {"errors": str(e)})
        except Exception as e:
            messages.error(request, 'Internal server error')
            return render(request, 'invoice/create_invoice.html', {"errors": str(e)})
