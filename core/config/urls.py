from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from rest_framework.routers import DefaultRouter

from rest_framework_swagger.views import get_swagger_view

from apps.users import views as uviews
from apps.parking import views as pviews


schema_view = get_swagger_view(title='ParkingLot API')


router = DefaultRouter()

router.register(r'users', uviews.UserViewSet, basename='users')
router.register(r'clients',uviews.ClientViewSet, basename='clients')
router.register(r'cars', pviews.CarViewSet, basename='cars')
router.register(r'places', pviews.PlaceViewSet, basename='places')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]