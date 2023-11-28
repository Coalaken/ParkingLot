from rest_framework import serializers

from .models import Car, Place
from apps.users.serializers import ClientSerializer


class CarSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(source='owner.user.phone')
    
    class Meta:
        model = Car
        fields = ('id', 'owner', 'number', 'model')



class PlaceSerializer(serializers.ModelSerializer):
    car = serializers.CharField(source='car.number')
    client = ClientSerializer()
    class Meta:
        model = Place
        fields = ('id', 'client', 'car', 'date_limit', 'payed')