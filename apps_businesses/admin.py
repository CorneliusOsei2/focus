from django.contrib import admin
from .models import Business, Job, Team

# Register your models here.
admin.site.register([Business, Team, Job])