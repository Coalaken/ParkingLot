from django.contrib.auth import authenticate

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.users.models import User, Client
from .serializers import UserSerializer, ExtendedClientSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(ModelViewSet):
	queryset = Client.objects.select_related('user').all()
	serializer_class = ExtendedClientSerializer


class LoginView(APIView):
    permission_classes = ()
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if (user := authenticate(username=username, password=password)) and user.is_active:
            return Response({'token': user.auth_token.key})
        return Response({'error': 'Wrong Credentials'}, status=status.HTTP_400_BAD_REQUEST)
