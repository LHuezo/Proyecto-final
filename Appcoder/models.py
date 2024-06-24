from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Opiniones(models.Model):
    titulo=models.CharField(max_length=50)
    sub=models.CharField(max_length=100)
    autor=models.CharField(max_length=20)
    cuerpo=models.TextField(max_length=500)



class Avatar(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    imagen= models.ImageField( upload_to="avatares",blank=True,null=True)
