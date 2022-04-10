from django.template import Context, Template, loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import familiares

# Create your views here.
def index(request):
    return HttpResponse("Mensaje de prueba")
    

def nombres(request):
  nomb = "Juancete"

  plantilla = loader.get_template('integrantes.html')
  plantilla_html = plantilla.render({"nombre_persona":nomb})

  return HttpResponse(plantilla_html)

def buscar(request):
  return render(request, 'buscar.html')

def buscar_integrante(request):
  if request.GET['fam']:
    nombre_busca = request.GET['fam']
    intefam = familiares.objects.filter(nombre__icontains=nombre_busca)
    return render(request, "resultado_busqueda.html", {"integrante_familia":intefam, "query": nombre_busca})
  else:
    mensaje = "No se paso ningun nombre a buscar"
  return HttpResponse(mensaje)