from django.shortcuts import render

from .models import Equipo
from .models import EquipoUsuario
from django.contrib import admin


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'referencia', 'marca', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('referencia',)


@admin.register(EquipoUsuario)
class EquipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'equipo', 'usuario', 'fecha_asignacion')
    list_filter = ('fecha_asignacion', 'usuario')