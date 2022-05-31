from django.shortcuts import render
from .models import Business

# Create your views here.
def businesses(request):
    ''' All businesses '''
    businesses = Business.objects.all()
    return render(request, 'businesses.html', {'businesses':businesses})

