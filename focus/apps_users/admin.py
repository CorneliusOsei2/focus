from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class UserAdminConfig(UserAdmin):
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name', 'username', 'contact', 'email')
    list_display = ('first_name', 'last_name', 'username', 'contact', 'email')

   


admin.site.register(CustomUser, UserAdminConfig)
