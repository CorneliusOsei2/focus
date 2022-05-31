from django.shortcuts import render
from models import Business
# Create your views here.
def businesses():
    ''' All businesses '''
    businesses = Business.objects.all()
    return render('businesses.html', businesses)