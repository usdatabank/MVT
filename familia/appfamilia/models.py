from django.db import models
from django.utils import timezone

# Creamos el modelo / tabla para la base de dato
class familiares(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(blank=True, null=True, max_length=60)
    cumple = models.DateField(auto_now=True)

def __str__(self):
    return self.nombre
