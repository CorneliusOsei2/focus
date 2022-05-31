from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

class UserViews:
    def login(request):
        
        return HttpResponse("Hiop")