from django.urls import path
from .views import invest

urlpatterns = [
    path('', invest, name='invest'),
]