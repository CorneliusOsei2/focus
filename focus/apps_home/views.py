from django.http import HttpResponse
from django.shortcuts import render
from .models import ContentsItem

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def contents(request):
    contents_items = ContentsItem.objects.all()

    return render(request, 'contents.html', {'contents': list(contents_items)})
