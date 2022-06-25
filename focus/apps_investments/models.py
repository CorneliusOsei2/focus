from django.db.models import Model, CharField, IntegerField, ManyToManyField
from apps_users.models import CustomUser
from apps_businesses.models import Business

# Create your models here.
class Investment(Model):
    user = ManyToManyField(CustomUser)
    business = ManyToManyField(Business)
    amount = IntegerField(default=0, null=False)
    period = IntegerField(default=1, null=False)

