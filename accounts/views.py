from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

from django.contrib.auth import get_user_model
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
        User = get_user_model()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

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
                return redirect('dashboard')

        return render(request, 'accounts/register.html')
