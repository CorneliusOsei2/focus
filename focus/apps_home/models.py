from django.db import models
# Create your models here.

class ContentsItem(models.Model):
    title =  models.CharField(max_length=100, null=False, default='')
    description = models.CharField(max_length=100, null=False, default='')
    destination = models.CharField(max_length=100, null=False, default='')
    position = models.CharField(max_length=10, null=False, default='')
    style = models.CharField(max_length=50, null=False, default='')
   

   