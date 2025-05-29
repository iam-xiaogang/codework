# author xiaogang
from rest_framework import serializers
from .models import ComputerRoom, Host, City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ComputerRoomNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerRoom
        fields = '__all__'


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'
