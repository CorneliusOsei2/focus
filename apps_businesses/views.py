import re
from django.shortcuts import render
from .models import Business, Team, Job

# Create your views here.
def businesses(request):
    ''' All businesses '''
    businesses = Business.objects.all()
    return render(request, 'businesses.html', {'businesses':businesses})

def business(request, business_id):
    ''' All businesses '''
    business = Business.objects.filter(id=business_id)
    return render(request, 'businesses.html', {'business':business})

def careers(request):
    team = Team.objects.filter(id=1).first()
    openings = team.job_set.all()
    return render(request, 'career_openings.html', {'openings': openings})
    
