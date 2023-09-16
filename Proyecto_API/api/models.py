from django.db import models

# Create your models here.

class Medicamento(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=50)
    dosis = models.IntegerField()
    precio = models.IntegerField()
    

