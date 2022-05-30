from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
class HomeViews:
    def home_top(request):
        return render(request, 'homeTop.html')

    def home_bottom(request):
        return render(request, 'homeBottom.html')
