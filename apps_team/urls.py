from django.urls import path
from .views import team

urlpatterns = [
    path('team', team, name='team'),
]
