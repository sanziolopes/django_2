from django.db import models

# Create your models here.
class Client(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    sexual_orientation = models.CharField(max_length=6)
    interest = models.TextField()
    photo = models.ImageField()
