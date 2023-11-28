from rest_framework import serializers

from .models import User, Client


class SimpleUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'phone')
  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.phone')
    class Meta:
        model = Client
        fields = ('user',)


class ExtendedClientSerializer(serializers.ModelSerializer):
    user = SimpleUserSerializer()
    
    class Meta:
        model = Client
        fields = ('id', 'user', )