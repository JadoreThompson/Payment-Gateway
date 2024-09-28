from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from validate_email import validate_email
import json


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


class RegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        data = json.loads(request.body)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')

        if not User.objects.filter(email=email).exists():
            if len(password) < 6:
                messages.error(request, "Password must be 6 characters")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email)
                user.set_password(password)
                user.save()
                messages.success(request, "Successfully signed up")
                return redirect('login')

        return render(request, 'accounts/register.html')
