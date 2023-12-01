from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import User, Client


class SimpleUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'phone')
  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}  
          
    def create(self, validated_data):
        user = User(
			phone=validated_data['phone'],
		)
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
        
        

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
