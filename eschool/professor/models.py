from django.db import models

# Create your models here.
class Proffesor(models.Model):
    fist_name = models.CharField(max_length=60)
    second_name = models.CharField(max_length=60)
    qualifiaction = models.CharField(max_length=60)  
    sexe = models.CharField(max_length=1)
    birth_day = models.DateField()
