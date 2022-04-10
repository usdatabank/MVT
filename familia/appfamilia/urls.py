from django.contrib import admin
from django.urls import path
from . import views

app_name = "appfamilia"
urlpatterns = [
    path('', views.index, name='index'),
    path('nombres/', views.nombres),
    path('buscaintegrante/', views.buscar_integrante),
    path('buscar/', views.buscar),
]