from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UsuarioTuristico
from .serializers import UsuarioTuristicoSerilizers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated



class UsuarioTuristicoApiView(APIView):

    @swagger_auto_schema(responses={200: UsuarioTuristicoSerilizers(many=True)})
    def get(self, request):
        usuarios = UsuarioTuristico.objects.all()
        serializer = UsuarioTuristicoSerilizers(usuarios, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UsuarioTuristicoSerilizers, responses={201: UsuarioTuristicoSerilizers})
    def post(self, request):
        serializer = UsuarioTuristicoSerilizers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsuarioTuristicoDetailView(APIView):

    @swagger_auto_schema(responses={200: UsuarioTuristicoSerilizers})
    def get(self, request, pk):
        try:
            usuario = UsuarioTuristico.objects.get(pk=pk)
        except UsuarioTuristico.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioTuristicoSerilizers(usuario)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=UsuarioTuristicoSerilizers, responses={200: UsuarioTuristicoSerilizers})
    def put(self, request, pk):
        try:
            usuario = UsuarioTuristico.objects.get(pk=pk)
        except UsuarioTuristico.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UsuarioTuristicoSerilizers(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            usuario = UsuarioTuristico.objects.get(pk=pk)
        except UsuarioTuristico.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CrearMiPerfilTuristicoView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=UsuarioTuristicoSerilizers,
        responses={201: UsuarioTuristicoSerilizers}
    )
    def post(self, request):
        # Verificar si ya tiene perfil
        if UsuarioTuristico.objects.filter(email=request.user.email).exists():
            return Response(
                {'error': 'Ya tienes un perfil turístico'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Crear perfil con los datos del usuario logueado
        data = request.data.copy()
        data['email'] = request.user.email  # Usar el email del usuario logueado

        serializer = UsuarioTuristicoSerilizers(data=data)
        if serializer.is_valid():
            usuario_turistico = serializer.save()
            return Response({
                'mensaje': 'Perfil turístico creado exitosamente',
                'usuario_turistico': UsuarioTuristicoSerilizers(usuario_turistico).data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={200: UsuarioTuristicoSerilizers})
    def get(self, request):
        """Ver mi perfil turístico"""
        try:
            usuario_turistico = UsuarioTuristico.objects.get(email=request.user.email)
            serializer = UsuarioTuristicoSerilizers(usuario_turistico)
            return Response(serializer.data)
        except UsuarioTuristico.DoesNotExist:
            return Response(
                {'error': 'No tienes perfil turístico. Crea uno con POST.'},
                status=status.HTTP_404_NOT_FOUND
            )