from django.urls import path
from .views import UserViews as uv

urlpatterns = [
    path('login', uv.login, name='login')
]