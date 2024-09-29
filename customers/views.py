import requests
import json

from django.http import JsonResponse

# Directory Modules
from tools import NATIVE_API
from .models import CustomCustomerModel

# Django Modules
from django.shortcuts import render
from django.views import View
from django.contrib import messages


class CreateCustomerView(View):
    def get(self, request) -> render:
        return render(request, 'customers/create_customers.html')

    def post(self, request):
        try:
            data = request.POST.dict()

            del data['csrfmiddlewaretoken']

            print(data)
            rsp = requests.post(f"{NATIVE_API}/customer/create", json=data)
            rsp_data = rsp.json()

            if rsp.status_code == 200:

                insert_data = {
                    "customer_id": rsp_data['customer']['id'],
                    'name': data['name'],
                    "email": rsp_data['customer']['email']
                }

                CustomCustomerModel.objects.create(**insert_data, user=request.user)
                messages.success(request, "Successfully created customer")
                return JsonResponse({"message": "success"}, status=200)
            else:
                return JsonResponse(status=500, data={"data": rsp_data})
        except Exception as e:
            return JsonResponse({"error": str(e), "type": f"{type(e)}"}, status=500)
