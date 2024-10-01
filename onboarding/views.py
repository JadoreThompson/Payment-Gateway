import json

import requests

# Dir
from tools import STRIPE_MICROSERVICE

# Django
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views import View


User = get_user_model()


class OnboardingView(View):
    def get(self, request):
        return render(request, 'onboarding/onboarding.html')

    def post(self, request):
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        if data['route'] == 'individual':
            date = request.POST.get('dob').split("-")
            post_data = {
                "individual": {
                    "address": {
                        "city": data['town'],
                        "country": data['country'],
                        'line1': data['address_line1'],
                        'line2': data["address_line2"],
                        "postal_code": data['postal_code']
                    },
                    'dob': {
                        'day': int(date[2]),
                        'month': int(date[1]),
                        'year': int(date[0])
                    },

                    # The 3 below should be prefilled into the form
                    'email': request.user.email,
                    "first_name": request.user.first_name,
                    'last_name': request.user.last_name,

                    "id_number": data['personal_id'],
                    'phone': data['phone_number'],
                },
                'stripe_account': request.user.stripe_account_id,
            }

            files = {
                "individual_file": request.FILES['individual_file']
            }

            # Microservice Request
            rsp = requests.post(f"{STRIPE_MICROSERVICE}/auth/update-user", data={"update_individual_request": json.dumps(post_data)}, files=files)
            rsp_data = rsp.json()


        if data['route'] == 'company':
            # Make sure to trim all values
            del data['route']
            data['stripe_account'] = request.user.stripe_account_id

            # Microservice Request
            rsp = requests.post(f"{STRIPE_MICROSERVICE}/auth/update-user", json=data)
            rsp_data = rsp.json()

        if data['route'] == 'bank':
            #print({"update_bank_info_request": json.dumps(data)})
            #print(json.dumps(data, indent=4))

            del data['route']
            data['stripe_account'] = request.user.stripe_account_id

            rsp = requests.post(
                f"{STRIPE_MICROSERVICE}/auth/update-user",
                data={"update_bank_info": json.dumps(data)})
            rsp_data = rsp.json()

        # Handling response
        if rsp.status_code == 200:
            return redirect('dashboard')
        if rsp.status_code == 500:
            messages.error(request, rsp_data['error'])
            return render(request, 'onboarding/onboarding.html')
        else:
            return render(request, 'onboarding/onboarding.html')