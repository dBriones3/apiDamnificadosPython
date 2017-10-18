from django.db import models

from personas.models import Personas

STATUS = (("1","Actual"),("0","Salio"))

# Create your models here.
class Lugares(models.Model) :
    calle = models.CharField(max_length=70)
    nombre = models.CharField(max_length=50)
    colonia = models.CharField(max_length=50)

class PersonasHasLugares(models.Model):
    fecha = models.DateField()
    status = models.CharField(choices=STATUS,max_length=20)
    lugares_id = models.ForeignKey(Lugares)
    personas_id = models.ForeignKey(Personas)