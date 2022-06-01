from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def register(request):
    """ Register a new user """
    
    return render(request, 'register.html')

def login(request):
    """ Log in a user """
    return HttpResponse("Hiop")