from django.apps import AppConfig
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Equipo
from .serializers import EquipoSerializer


class InventarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventario'

class EquipoListView(APIView):
    def get(self, request):
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        return Response(serializer.data)