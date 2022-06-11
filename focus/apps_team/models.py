from django.db.models import *

# Create your models here.
class Team(Model):
    first_name = CharField(null=False)
    last_name = CharField(null=False)
    image = CharField(null=False)
    role = CharField(null=False)
    statement = CharField(null=False)
