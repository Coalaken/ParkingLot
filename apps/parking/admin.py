from django.contrib import admin

from . import models


@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['owner', 'number', 'model']
    raw_id_fields = ['owner']
    list_editable = ['number', 'model']


@admin.register(models.Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['client', 'car', 'date_limit', 'payed']
    raw_id_fields = ['client', 'car']
    list_editable = ['date_limit', 'payed']