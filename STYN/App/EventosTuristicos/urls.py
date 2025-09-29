from django.urls import  path, include
from rest_framework.routers import  DefaultRouter
from .ModelViewSet import EventosTuristicosViewSet


router = DefaultRouter()
router.register(r'eventosturisticos',EventosTuristicosViewSet, basename='eventoturistico')

urlpatterns = [

    path('', include(router.urls)),

]
