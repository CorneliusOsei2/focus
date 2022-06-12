from django.db.models import Model, CharField
# Create your models here.
class ContentsItem(Model):
    title =  CharField(max_length=100, null=False, default='')
    description = CharField(max_length=100, null=False, default='')
    destination = CharField(max_length=100, null=False, default='')
    style = CharField(max_length=100, null=False, default='')

    

   