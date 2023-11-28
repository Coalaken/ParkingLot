import datetime
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone

from apps.users.models import Client


class Car(models.Model):
    owner = models.ForeignKey(
		Client, related_name="cars", on_delete=models.CASCADE
	)
    number = models.CharField(max_length=10)
    model = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.owner}: {self.model} [{self.number}]"


class PayedPlaceManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(payed=True)
    

class Place(models.Model):
    
    objects = models.Manager()
    _payed = PayedPlaceManager()
    
    client = models.ForeignKey(
		Client, related_name="parking_places", on_delete=models.CASCADE
	)
    car = models.ForeignKey(
		Car, related_name="parking_places", on_delete=models.CASCADE
	)
    date_limit = models.DateTimeField(
        default=timezone.now() + datetime.timedelta(days=1)
    )
    payed = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Place: {self.id}"