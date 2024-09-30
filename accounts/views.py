import json
import requests

# Dir
from tools import STRIPE_MICROSERVICE

# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from validate_email import validate_email


User = get_user_model()


class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        if not validate_email(email):
            return JsonResponse({'email_error': 'email should only container alphanumeric characters'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Email already exists'}, status=409)
        return JsonResponse({'email_valid': True}, status=200)


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        else:
            login(request, user)
            messages.success(request, 'Successfully logged in')
            return redirect('dashboard')



class RegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        email = request.POST.get('email')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')

        if not User.objects.filter(email=email).exists():
            data = request.POST.dict()
            del data['csrfmiddlewaretoken']
            data['tos_shown_and_accepted'] = True
            data['password'] += "10@@"

            # Microservice Request
            rsp = requests.post(f"{STRIPE_MICROSERVICE}/auth/signup", json=data)
            rsp_data = rsp.json()

            if rsp.status_code == 200:
                messages.success(request, rsp_data['message'])
                user = User.objects.create_user(
                    first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), email=email,
                    stripe_account_id=rsp_data['account']['account']
                )
                user.set_password(request.POST.get('password'))
                user.save()
                messages.success(request, "Successfully signed up")
                login(request, user)
                return redirect('onboard_user')

        return render(request, 'accounts/register.html')


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')
