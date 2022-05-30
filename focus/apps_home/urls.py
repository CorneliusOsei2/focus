from django.urls import path
from .views import HomeViews as hv

urlpatterns = [
    path('', hv.home_top, name='home_top'),
    path('content', hv.home_bottom, name='home_bottom')
]