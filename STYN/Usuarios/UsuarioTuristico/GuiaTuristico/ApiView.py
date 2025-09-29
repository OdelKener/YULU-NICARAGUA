from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, permissions
from Usuarios.UsuarioGuia.models import GuiaTuristico
from Usuarios.UsuarioGuia.serializers import GuiaTuristicoRegisterSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated



class GuiaTuristicoCreateView(generics.CreateAPIView):
    queryset = GuiaTuristico.objects.all()
    serializer_class = GuiaTuristicoRegisterSerializer
    permission_classes = [permissions.IsAuthenticated]
