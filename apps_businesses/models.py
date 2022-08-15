from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE

# Create your models here.
class Business(Model):
    title = CharField(max_length=100, default="")
    number = IntegerField(default=1)
    description = CharField(max_length=100, default="")
    growth_rate = IntegerField(default=100)
    locations = CharField(max_length=100)
    
class Team(Model):
    name = CharField(max_length=100, default="")
    lead = CharField(max_length=100, default="")

class Job(Model):
    title = CharField(max_length=200, default="")
    salary = IntegerField(default=0)
    team = ForeignKey(Team, on_delete=CASCADE)
    description = CharField(max_length=5000, default="")
    qualifications = CharField(max_length=20000, default="")
    responsibilities = CharField(max_length=20000, default="")
    openings = IntegerField(default=0)
    period = CharField(max_length=200, default="")