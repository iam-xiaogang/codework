# author xiaogang

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import City,Host,ComputerRoom
from .serializers import CitySerializer, ComputerRoomNameSerializer, HostSerializer
import subprocess


class AllCityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ComputerRoomNameViewSet(viewsets.ModelViewSet):
    queryset = ComputerRoom.objects.all()
    serializer_class = ComputerRoomNameSerializer


class AllHostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    @action(detail=True, methods=['get'])
    def ping(self, request, pk=None):
        host = self.get_object()
        try:
            result = subprocess.run(["ping", "-c", "1", host.ip_address], stdout=subprocess.PIPE)
            reachable = result.returncode == 0
        except Exception:
            reachable = False
        return Response({"reachable": reachable})
