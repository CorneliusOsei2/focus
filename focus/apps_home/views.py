from django.http import HttpResponse
from django.shortcuts import render
from .models import ContentsItem

# Create your views here.
class HomeViews:
    def home_top(request):
        return render(request, 'home_top.html')

    def home_bottom(request):
        return render(request, 'home_bottom.html')
