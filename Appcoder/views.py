from django.shortcuts import render
from .models import Avatar,Opiniones
from django.http import HttpResponse
from .forms import opinionformulario
from django.utils import timezone

# Create your views here.

def index(req):

    return render(req,"index.html",{})

def significado_de_figuras(req):

     return render(req,"significado.html",{})

def posicionamiento_de_notas(req):

     return render(req,"Posicionamiento.html",{})

def compas(req):

     return render(req,"compas.html",{})

def escala_de_acordes(req):

     return render(req,"escalaDeAcordes.html",{})

def danos_tu_opinion(req):
    
    return render(req,"danostuopinion.html",{})

def opinion_formulario(req):

     if req.method == 'post':

          miFormulario = opinionformulario(req.POST)

          if miFormulario.is_valid():

               miFormulario.save()

               return render(req, "opiniones.html")
    
     else:
      
          miFormulario = opinionformulario()

          return render(req ,"datuopinion.html", {"miFormulario":miFormulario})
  
def opiniones(req):

    return render(req,"Opiniones.html",{})

def leerOpiniones(req):
    
    opinioneS=Opiniones.objects.all()
    contexto={"opiniones":opinioneS}
    return render(req,"opiniones.html",contexto)

def eliminar_opinion(req, id):

    opinion = Opiniones.objects.get(id=id)
    opinion.delete()

    mis_opiniones = Opiniones.objects.all()

    contexto2={"opiniones":mis_opiniones}

    return render(req, "opiniones.html",contexto2)



