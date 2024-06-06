from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    fechaDeNacimiento=models.DateField()
    dni=models.IntegerField()

class Instrumento(models.Model):
    Tipo=models.CharField(max_length=100)
    AñosDePractica=models.IntegerField()

class CancionAAprender(models.Model):
    nombreDeCancion=models.CharField(max_length=100)
    fechaDeLanzamiento=models.DateField()
    Autor=models.IntegerField()

