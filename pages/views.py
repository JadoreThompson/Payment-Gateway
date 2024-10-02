import json

import requests

from tools import STRIPE_MICROSERVICE

from django.views import View
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'pages/index.html')


@login_required
class DashboardView(View):
    def get(self, request):
        post_data = {'stripe_account': request.user.stripe_account_id}

        rsp = requests.post(f"{STRIPE_MICROSERVICE}/payments/get-stats", json=post_data)
        content = rsp.json()

        content['todays_sales'] = "{:.2f}".format(content['todays_sales'])

        print(json.dumps(content, indent=4))

        return render(request, 'pages/dashboard.html', content)
