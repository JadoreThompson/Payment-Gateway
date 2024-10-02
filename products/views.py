import requests

# Dir
from tools import STRIPE_MICROSERVICE
from .models import CustomProductsModel

# Django
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
class ProductCreateView(View):
    def get(self, request):
        return render(request, 'products/create_product.html')

    def post(self, request):
        try:
            data = request.POST.dict()
            del data['csrfmiddlewaretoken']
            data['unit_amount'] = int(float(data['unit_amount']) * 100)

            # Microservice request
            rsp = requests.post(f"{STRIPE_MICROSERVICE}/products/create", json=data)
            rsp_data = rsp.json()

            if rsp.status_code == 200:
                insert_data = {
                    "product_id": rsp_data['product']['id'],
                    "price": rsp_data["product"]["price"],
                    "name": rsp_data["product"]["name"],
                    "description": rsp_data['product'].get('description', None)
                }
                CustomProductsModel.objects.create(user=request.user, **insert_data)
                return redirect('products')

            raise Exception(rsp_data['error'])
        except Exception as e:
            print("Error: ", str(e))
            messages.error(request, "Something went wrong, please try again")
            return render(request, "products/create_products.html")
