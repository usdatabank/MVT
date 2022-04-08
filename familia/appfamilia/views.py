from django.shortcuts import render
from django.http import HttpResponse
from .models import familiares

# Create your views here.
def index(request):
    return HttpResponse("Mensaje de prueba")
    
def integrante(request):
  familiar = familiares.objects.filter(nombre__contains='andrea')
  return render(request, 'integrantes.html', {})