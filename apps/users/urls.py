from django.urls import path

from rest_framework.routers import DefaultRouter

from . import views


user_router = DefaultRouter()
client_router = DefaultRouter()

user_router.register(r'users', views.UserViewSet, basename='users')
client_router.register(r'clients',views.ClientViewSet, basename='clients')

urlpatterns = []

urlpatterns += user_router.urls
urlpatterns += client_router.urls
