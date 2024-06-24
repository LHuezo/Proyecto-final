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

     if req.method == "POST":
          miFormulario = opinionformulario(req.POST)

          print(miFormulario)
               
          data=miFormulario.cleaned_data

          miopinion=Opiniones (titulo=data["titulo"],sub=data["sub"],autor=data["autor"],cuerpo=data["cuerpo"])
          miopinion.save()

          return render(req, "index.html",{})
    
     else:
      
          miFormulario = opinionformulario()
          contexto={"miFormulario":miFormulario}

          return render(req ,"datuopinion.html", contexto)
  
def verOpinion(req,id):
     opinion = Opiniones.objects.get(id=id)
     return render(req,"opiniondepersona.html",{"opinion":opinion})

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



