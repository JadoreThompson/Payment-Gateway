from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegistrationView.as_view(), name='register'),
    path('validate-email', csrf_exempt(views.EmailValidationView.as_view()), name='validate_email'),
    path('logout', views.Logout.as_view(), name='logout')
]
