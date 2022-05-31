from django.db.models import Model, CharField, IntegerField

# Create your models here.
class User(Model):
    first_name = CharField(max_length=100, default="")
    last_name = CharField(max_length=100, default="")
    username = CharField(max_length=100, default="")
    dob = IntegerField()

    '''
    user -> investments
    user -> sales

    '''




