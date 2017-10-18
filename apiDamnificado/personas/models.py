from django.db import models

SEXOS = (("M","MUJER"),("H","Hombre"),("I", "Indefinido"))
TIPOSPERSONAS = (("Voluntario","Voluntario"), ("Damnificado","Damnificado"), ("Otro","Otro"))
# Create your models here.

class Personas(models.Model) :
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    sexo = models.CharField(choices=SEXOS, max_length=2)
    tipo_de_personas = models.CharField(choices=TIPOSPERSONAS,max_length=50)