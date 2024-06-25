from django.shortcuts import render
from .models import Avatar,Opiniones
from django.http import HttpResponse
from .forms import opinionformulario,UserRegisterForm
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def inicio(req):

    return render(req,"inicio.html",{})

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

def loginuser(req):
     if req.method == "POST":
          form=AuthenticationForm(req,data=req.POST)
          if form.is_valid():
               usuario=form.cleaned_data.get("username")
               contraseña=form.cleaned_data.get("password")

               user=authenticate(username=usuario,password=contraseña)

               if user is not None:
                    login(req,user)
                    return render(req,"inicio.html",{"nombre":usuario})
               else:
                    form=AuthenticationForm()
                    return render(req,"index.html",{"form":form,"mensaje":"El usuario ingrsado no existe o Los datos ingrsados no son correctos"})
          else:
               form=AuthenticationForm()
               return render(req,"index.html",{"form":form,"mensaje":"El usuario ingrsado no existe o Los datos ingrsados no son correctos"})
     else:
          form=AuthenticationForm()
          return render(req,"index.html",{"form":form})
     
def registeruser(req):
     if req.method == "POST":
          form=UserRegisterForm(req.POST)
          if form.is_valid():
               username=form.cleaned_data("username")
               form.save()
               return render(req,"index.html",{"mensaje1":"Su usuario se creo con exito"})
     else:
          form=UserRegisterForm()
     return render(req,"registro.html",{"form":form})



