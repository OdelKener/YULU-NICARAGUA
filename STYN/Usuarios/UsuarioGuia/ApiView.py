# Usuarios/UsuarioGuia/ApiView.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import GuiaTuristico
from .serializers import GuiaTuristicoRegisterSerializer
from rest_framework.permissions import IsAuthenticated
from Usuarios.UsuarioTuristico.models import UsuarioTuristico
from Usuarios.UsuarioGuia.serializers import GuiaTuristicoListSerializer

class RegistroGuiaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            usuario_turistico = UsuarioTuristico.objects.get(email=request.user.email)
        except UsuarioTuristico.DoesNotExist:
            return Response(
                {"error": "Debes tener un perfil turístico antes de registrar un guía."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = GuiaTuristicoRegisterSerializer(data=request.data)
        if serializer.is_valid():
            guia = serializer.save(usuario=usuario_turistico)  # ← asignar el perfil correcto

            # Notificar admin
            self.notificar_admin(guia)

            return Response({
                "mensaje": "Perfil de guía creado. En revisión por administración.",
                "guia": GuiaTuristicoRegisterSerializer(guia).data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def notificar_admin(self, guia):
        print(f"Nuevo guía para revisión: {guia.usuario.email}")  # usuario_turistico

class ListaGuiasAprobadosView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        guias = GuiaTuristico.objects.filter(aprobado=True)
        serializer = GuiaTuristicoListSerializer(guias, many=True)
        return Response(serializer.data)
