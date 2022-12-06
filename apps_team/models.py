from django.db.models import *

# Create your models here.
class Team(Model):
    first_name = CharField(max_length=100, null=False)
    last_name = CharField(max_length=100, null=False)
    username = CharField(max_length=100, null=False)
    image = CharField(max_length=100, null=False)
    role = CharField(max_length=100, null=False)
    statement = CharField(max_length=100, null=False)
    style = CharField(max_length=100, null=False)
