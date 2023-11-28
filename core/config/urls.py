from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.users import views as uviews
from apps.parking import views as pviews

router = DefaultRouter()

router.register(r'users', uviews.UserViewSet, basename='users')
router.register(r'clients',uviews.ClientViewSet, basename='clients')
router.register(r'cars', pviews.CarViewSet, basename='cars')
router.register(r'places', pviews.PlaceViewSet, basename='places')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
