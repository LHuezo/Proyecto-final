from django.http import HttpResponse
from django.template import Template
def saludo(req):
    return HttpResponse("Hola mundo")

# def probando_template(req):
#     mihtml=open("C:\Users\User\Desktop\CODERHOUSE\TerceraPre-entregaHuezocarpeta\Appcoder\templates\template.html")
#     plantilla= Template(mihtml.read)
#     mihtml.close()
#     plantilla.render()