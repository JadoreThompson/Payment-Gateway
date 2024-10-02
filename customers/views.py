import requests
import json

from django.http import JsonResponse

# Directory Modules
from tools import STRIPE_MICROSERVICE
from .models import CustomCustomerModel

# Django Modules
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
class CreateCustomerView(View):
    def get(self, request) -> render:
        return render(request, 'customers/create_customers.html')

    def post(self, request):
        try:
            data = request.POST.dict()

            del data['csrfmiddlewaretoken']

            # Microservice Request
            rsp = requests.post(f"{STRIPE_MICROSERVICE}/customer/create", json=data)
            rsp_data = rsp.json()

            # Handling Response
            if rsp.status_code == 200:
                insert_data = {
                    "customer_id": rsp_data['customer']['id'],
                    'name': data['name'],
                    "email": rsp_data['customer']['email']
                }

                CustomCustomerModel.objects.create(**insert_data, user=request.user)
                messages.success(request, "Successfully created customer")
                return redirect('customers')
            else:
                print(f"Create Customer: {rsp_data['error']}")
                messages.error(request, message="Something went wrong")
                return render(request, "customers/create_customer.html")
        except Exception as e:
            return JsonResponse({"error": str(e), "type": f"{type(e)}"}, status=500)
