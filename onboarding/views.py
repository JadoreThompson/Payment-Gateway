from django.shortcuts import render

from onboarding.forms import SignUpForm


# Create your views here.
def login(request):
    return render(request, 'login.html')


def signup(request):
    form = SignUpForm()
    return render(request, 'signup.html', {"form": form})


def onboarding(request):
    return render(request, 'onboarding.html')
