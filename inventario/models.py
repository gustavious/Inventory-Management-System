from django.contrib.auth.models import User
from django.db import models

class Equipo(models.Model):
    referencia = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    memoria = models.CharField(max_length=100)
    disco = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

class EquipoUsuario(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_asignacion = models.DateField()
    fecha_entrega = models.DateField(null=True, blank=True)