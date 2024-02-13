from django.shortcuts import render

from .models import Equipo
from .models import EquipoUsuario
from django.contrib import admin

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EquipoSerializer


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id', 'referencia', 'marca', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('referencia',)


@admin.register(EquipoUsuario)
class EquipoUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'equipo', 'usuario', 'fecha_asignacion')
    list_filter = ('fecha_asignacion', 'usuario')


class EquipoListView(APIView):
    def get(self, request):
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)
