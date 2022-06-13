from django.urls import path
from .views import businesses, business

urlpatterns = [
    path("businesses", businesses, name='businesses'),
    path("businesses/<int:business_id>/", business, name='businesses'),
]
