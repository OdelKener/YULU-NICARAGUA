from django.urls import  path, include
from rest_framework.routers import  DefaultRouter
from .ApiView import UsuarioTuristicoApiView
from .ModelViewSet import UsuarioTuristicoViewSet
from .models import UsuarioTuristico
# from Usuarios.UsuarioTuristico.GuiaTuristico.ApiView import GuiaTuristicoCreateView
from .ApiView import (
    UsuarioTuristicoApiView,
    UsuarioTuristicoDetailView,
    CrearMiPerfilTuristicoView, # ← NUEVA IMPORTACIÓN


)

router = DefaultRouter()
router.register(r'usuarioturistico',UsuarioTuristicoViewSet, basename='usuarioturistico')

urlpatterns = [

    path('', include(router.urls)),
    path('usuarios/', UsuarioTuristicoApiView.as_view(), name='usuarios-list'),
    path('usuarios/<int:pk>/', UsuarioTuristicoDetailView.as_view(), name='usuarios-detail'),
    path('mi-perfil/', CrearMiPerfilTuristicoView.as_view(), name='mi-perfil'),
    path('guia/', include('Usuarios.UsuarioTuristico.GuiaTuristico.urls')),

]
