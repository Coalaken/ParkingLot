from rest_framework.viewsets import ModelViewSet

from apps.users.models import User, Client
from .serializers import UserSerializer, ExtendedClientSerializer
from rest_framework.permissions import IsAdminUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, ]


class ClientViewSet(ModelViewSet):
	queryset = Client.objects.select_related('user').all()
	serializer_class = ExtendedClientSerializer
	permission_classes = [IsAdminUser, ]