from django.db.models import CharField, EmailField, IntegerField, BooleanField
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
    
    def create_user(self, first_name, last_name, username, contact, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            contact=contact,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, first_name, last_name, username, contact, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        user = self.create_user(
            first_name,
            last_name,
            username,
            contact,
            email,
            password,
            **other_fields
        )

        return user



class CustomUser(AbstractUser, PermissionsMixin):
    first_name = CharField(max_length = 50, blank=False)
    last_name = CharField(max_length = 50, blank=False)
    username = CharField(max_length = 50, unique = True)
    contact = IntegerField(blank=False)
    email = EmailField(_('email address'), unique = True, blank=False)
    is_active= BooleanField(default=False)
    is_staff= BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact', 'email']
    objects = CustomUserManager()

    def __str__(self):
        return "{}".format(self.email)
