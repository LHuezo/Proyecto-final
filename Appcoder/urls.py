

from django.urls import path
from Proyectopara3erentrega.views import saludo
from Appcoder.views import index,significado_de_figuras,posicionamiento_de_notas,compas,escala_de_acordes,leerOpiniones,eliminar_opinion,opinion_formulario

urlpatterns = [
    path('saludar/', saludo),
    path("index/",index,name="index" ),
    path("figures meaning/",significado_de_figuras,name="significadodefiguras"),
    path("notes positioning/",posicionamiento_de_notas,name="posicionamientodenotas"),
    path("compas/",compas,name="compas"),
    path("chord scale/",escala_de_acordes,name="escaladeacordes"),
    path("route pages/",leerOpiniones,name="lasopiniones"),
    path("eliminaropinion/<int:id>",eliminar_opinion,name="eliminacion"),
    path("formulario/",opinion_formulario,name="opinionformulario")
 ]
