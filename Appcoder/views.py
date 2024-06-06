from django.shortcuts import render
from .models import Estudiante
from django.http import HttpResponse
# Create your views here.
def estudiante(req):
    nuevo_Estudiante = Estudiante( nombre="Agustina",apellido="huezo",fechaDeNacimiento="1999-06-18",dni=100000)
    nuevo_Estudiante.save()

    return HttpResponse(f"""
    <p> Estudiante:{nuevo_Estudiante.nombre} fue registrado! </p>
""")

def lista_estudiantes(req):

    lista =Estudiante.objects.all()

    return render(req,"lista_estudiantes.html",{"lista_estudiantes": lista})