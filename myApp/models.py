from django.db import models

# Create your models here.

class MyItem(models.Model):
    title = models.CharField(max_length=200)
    descript = models.CharField(max_length=400) 
