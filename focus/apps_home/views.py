from django.http import HttpResponse
from django.shortcuts import render
from .models import ContentsItem

# Create your views here.
def home(request):
    """ Home page """
    contents_items = ContentsItem.objects.all()
    return render(request, 'home.html', {'contents': list(contents_items)})
