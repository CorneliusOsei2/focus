from django.urls import path
from .views import team, contact

urlpatterns = [
    path('team', team, name='team'),
    path('contact', contact, name='contact')
]
