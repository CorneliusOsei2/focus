from django.shortcuts import render
from .models import Team

# Create your views here.
def team(request):

    team = Team.objects.all()
    return render(request, 'team.html', {'team': team})