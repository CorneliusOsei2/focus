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
    marketing_openings = Team.objects.filter(name='Marketing').first().job_set.all()
    agriculture_openings = Team.objects.filter(name='Agriculture').first().job_set.all()
    construction_openings = Team.objects.filter(name='Construction').first().job_set.all()
    return render(request, 
        'career_openings.html', 
        {'marketing_openings': marketing_openings, 
        'agriculture_openings': agriculture_openings,
        'construction_openings':construction_openings})
    
