import json
import requests
import aiohttp

from tools import NATIVE_API
from invoice.models import CustomInvoiceModel

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View


def create_invoice(request):
    """
    :param request:
    :return: Creates a draft invoice and inserts basic invoice data in Table
    """
    try:
        data = request.POST.dict()
        print("^^^^^^^^^^^")
        print(data)
        print("^^^^^^^^^^^")
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
            'due_date': data['due_date']
        }

        rsp = requests.post(f"{NATIVE_API}/payments/invoice/create", json=post_data)
        rsp_data = rsp.json()

        if rsp.status_code == 500:
            messages.error(request, rsp_data['message'])
            return render(request, 'invoice/create_invoice.html')

        if rsp.status_code == 200:
            invoice_data = {
                'invoice_id': rsp_data['invoice']['id'], 'amount': int(rsp_data['invoice']['amount']),
                'customer_name': data['customer_name'], 'customer_email': data['customer_email']
            }
            invoice = CustomInvoiceModel.objects.save(user=request.user, **invoice_data)
            invoice.save()

            messages.success(request, 'Successfully created Invoice')
            return redirect('invoice')
        return redirect('dashboard')
    except json.JSONDecodeError as e:
        messages.error(request, 'Internal server error')
        raise json.JSONDecodeError
    except Exception as e:
        messages.error(request, 'Internal server error')
        raise Exception(e)


class CreateInvoiceView(View):
    def get(self, request):
        return render(request, 'invoice/create_invoice.html')

    def post(self, request):
        """
        :param request:
        :return: Finalized invoice sent to user
        """
        try:
            create_invoice(request)
        except json.JSONDecodeError as e:
            return JsonResponse({'message': 'Error converting data to JSON', 'error': str(e)}, status=500)
        except Exception as e:
            messages.error(request, 'Internal server error')
            return JsonResponse({'error': 'idk', 'type': f"{type(e)}"})
