from django.http import HttpResponse
from django.shortcuts import render
from .models import ContentsItem

# Create your views here.
def landing(request):
    """ Landing page """
    contents_items = ContentsItem.objects.all()
    return render(request, 'landing.html', {'contents': list(contents_items)})

def contents(request):
    """ Contents page """
    contents_items = ContentsItem.objects.all()
    return render(request, 'contents.html', {'contents': list(contents_items)})
