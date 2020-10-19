from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render


def index(request):
    # View code here...
    return render(request, 'templates/home.html')
