from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .ModelViewSet import SitiosTuristicosViewSet
from App.SitiosTuristicos.views import sitios_turisticos
from . import views

router = DefaultRouter()
router.register(r'sitiosturisticos', SitiosTuristicosViewSet, basename='sitiosturisticos')

urlpatterns = [
    path('', include(router.urls)),
    path('sitios-turisticos/', views.sitios_turisticos, name='sitios_turisticos'),
]

