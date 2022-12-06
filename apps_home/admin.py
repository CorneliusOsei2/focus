from django.contrib import admin
from .models import ContentsItem, Highlight

# Register your models here.
admin.site.register((ContentsItem, Highlight))