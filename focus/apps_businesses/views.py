from django.shortcuts import render
from .models import Business

# Create your views here.
def businesses(request):
    ''' All businesses '''
    businesses = Business.objects.all()
    return render(request, 'businesses.html', {'businesses':businesses})

def business(request, business_id):
    ''' All businesses '''
    business = Business.objects.filter(id=business_id)
    return render(request, 'businesses.html', {'business':business})

