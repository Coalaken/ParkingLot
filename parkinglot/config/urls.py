from django.contrib import admin
from django.urls import path

from django.conf import settings


print(settings.DEBUG)

urlpatterns = [
    path('admin/', admin.site.urls),
]
