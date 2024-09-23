from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def onboarding(request):
    return render(request, 'onboarding.html')
