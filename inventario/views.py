from django.shortcuts import render

from .models import Equipo
from .models import EquipoUsuario
from django.contrib import admin

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EquipoSerializer

class EquipoListView(APIView):
    def get(self, request):
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)
