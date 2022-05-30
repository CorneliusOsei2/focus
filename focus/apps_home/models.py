from django.db import models
# Create your models here.

class ContentsItem(models.Model):
    description = models.CharField(max_length=100)
    position = models.CharField(max_length=10)
    color = models.CharField(max_length=10)

   