from django.db.models import Model, CharField, IntegerField

# Create your models here.
class Business(Model):
    title = CharField(max_length=100, default="")
    number = IntegerField(default=1)
    description = CharField(max_length=100, default="")
    growth_rate = IntegerField(default=100)
    locations = CharField(max_length=100)
    
