from django.contrib import admin

from . import models


# check how @register works
@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user']