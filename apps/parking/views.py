from django.db.models import Prefetch

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Car, Place
from apps.users.models import Client
from .serializers import CarSerializer, PlaceSerializer


class CarViewSet(ModelViewSet):
    queryset = Car.objects.select_related('owner', 'owner__user').all()
    serializer_class = CarSerializer


class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.prefetch_related(
        Prefetch(
			'client', queryset=Client.objects.select_related('user').only('user__phone').all()
		),
		Prefetch(
			'car', queryset=Car.objects.select_related('owner').only('number', 'owner__user__id').all()
		) 
	).all()
    serializer_class = PlaceSerializer
    
    @action(detail=True, methods=['post', 'get'])
    def pay(self, request, pk=None):
        place = self.get_object()
        place.payed = True if not place.payed else False
        place.save()
        return Response(place.payed)
