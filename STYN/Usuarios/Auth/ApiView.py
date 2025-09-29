from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import logout
from .serializers import RegistroSerializer, LoginSerializer, UserSerializer
from Usuarios.UsuarioTuristico.models import UsuarioTuristico
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from Usuarios.Auth.models import Userabs




from rest_framework.authtoken.models import Token

class RegistroView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=RegistroSerializer, responses={201: UserSerializer})
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generar token automáticamente
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'user': UserSerializer(user).data,
                'token': token.key,  # Devolvemos el token
                'mensaje': f'¡Bienvenido {user.first_name}! Registro exitoso.'
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # aceptar email o username en el campo 'email' (como venías usando)
        email_or_username = request.data.get("email")
        password = request.data.get("password")

        if not email_or_username or not password:
            return Response({"error": "Faltan credenciales"}, status=status.HTTP_400_BAD_REQUEST)

        # 1) Intentar authenticate() directo (por username)
        user = authenticate(request, username=email_or_username, password=password)

        # 2) Si no se autenticó, intentar buscar por email y comprobar password manualmente
        if user is None:
            try:
                user_obj = Userabs.objects.get(email=email_or_username)
            except Userabs.DoesNotExist:
                # también intentar buscar por username si email_or_username no era email
                try:
                    user_obj = Userabs.objects.get(username=email_or_username)
                except Userabs.DoesNotExist:
                    return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

            # ahora validar contraseña manualmente
            if not user_obj.check_password(password):
                return Response({"error": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

            user = user_obj

        # Si llegamos aquí, user está autenticado
        # Crear o obtener token
        token, _ = Token.objects.get_or_create(user=user)

        # Crear/obtener perfil turístico asociado (por email) — con defaults seguros
        usuario_turistico, created = UsuarioTuristico.objects.get_or_create(
            email=user.email,
            defaults={
                "name": user.first_name or user.username,
                "lastname": user.last_name or "",
                "sexo": "M",
                "pais": "NI"
            }
        )

        # Respuesta
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
            "perfil_turistico": {
                "id": usuario_turistico.id,
                "name": usuario_turistico.name,
                "lastname": usuario_turistico.lastname,
                "pais": str(usuario_turistico.pais) if hasattr(usuario_turistico, 'pais') else usuario_turistico.pais
            },
            "token": token.key,
            "mensaje": f"Bienvenido {user.first_name or user.username}"
        }, status=status.HTTP_200_OK)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Eliminar token
        Token.objects.filter(user=request.user).delete()
        logout(request)

        return Response({'mensaje': 'Sesión cerrada exitosamente'})

class RegistroTemplateView(APIView):
    def get(self, request):
        return render(request, 'registro.html')  # Template de registro


class PerfilView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Obtener perfil turístico también
        try:
            usuario_turistico = UsuarioTuristico.objects.get(email=request.user.email)
            perfil_data = {
                'usuario_auth': UserSerializer(request.user).data,
                'usuario_turistico': {
                    'id': usuario_turistico.id,
                    'name': usuario_turistico.name,
                    'lastname': usuario_turistico.lastname,
                    'sexo': usuario_turistico.sexo,
                    'pais': str(usuario_turistico.pais)
                }
            }
        except UsuarioTuristico.DoesNotExist:
            perfil_data = {
                'usuario_auth': UserSerializer(request.user).data,
                'usuario_turistico': None
            }

        return Response(perfil_data)