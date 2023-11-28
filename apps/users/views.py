from rest_framework.viewsets import ModelViewSet

from apps.users.models import User, Client
from .serializers import UserSerializer, ExtendedClientSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ClientViewSet(ModelViewSet):
	queryset = Client.objects.select_related('user').all()
	serializer_class = ExtendedClientSerializer