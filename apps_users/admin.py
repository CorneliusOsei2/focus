from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class UserAdminConfig(UserAdmin):
    ordering = ('first_name',)
    search_fields = ('first_name', 'last_name', 'username', 'contact', 'email')
    list_display = ('first_name', 'last_name', 'username', 'contact', 'email')
    list_filter = ('first_name', 'last_name', 'username', 'contact', 'email', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'contact', 'email',)}),
        ('Permissions', {'fields': ('is_superuser', 'is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'first_name', 'last_name', 'username', 'contact', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
        })
    )

   
   


admin.site.register(CustomUser, UserAdminConfig)
