from django.urls import  path, include
from rest_framework.routers import  DefaultRouter
from .ApiView import RegistroGuiaView
from .ModelViewSet import GuiaTuristicoViewSet
from .models import GuiaTuristico
from Usuarios.UsuarioGuia.ApiView import ListaGuiasAprobadosView

router = DefaultRouter()
router.register(r'guiaturistico',GuiaTuristicoViewSet, basename='guiaturistico')

urlpatterns = [

    path('registro/', RegistroGuiaView.as_view(), name='guia-registro'),
    path('', include(router.urls)),
    path('aprobados/', ListaGuiasAprobadosView.as_view(), name='guias-aprobados'),

]
