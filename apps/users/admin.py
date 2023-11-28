from django.contrib import admin

from . import models


admin.site.register(models.User)

# check how @register works
@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user']