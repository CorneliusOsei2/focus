from django.urls import path
from views import businesses

urlpatterns = [
    path("businesses", businesses, name=businesses)
]
