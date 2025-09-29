# App/Departamento/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import Departamento
from .serializers import DepartamentoSerializers  # Asumo que crearás este serializer

class DepartamentoApiView(APIView):

    @swagger_auto_schema(responses={200: DepartamentoSerializers(many=True)})
    def get(self, request):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializers(departamentos, many=True)
        return Response(serializer.data)

    # IMPORTANTE: Como los departamentos son fijos, probablemente NO quieras permitir POST.
    # Pero por si acaso, aquí está la implementación.
    @swagger_auto_schema(request_body=DepartamentoSerializers, responses={201: DepartamentoSerializers})
    def post(self, request):
        serializer = DepartamentoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartamentoDetailView(APIView):

    @swagger_auto_schema(responses={200: DepartamentoSerializers})
    def get(self, request, pk):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartamentoSerializers(departamento)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=DepartamentoSerializers, responses={200: DepartamentoSerializers})
    def put(self, request, pk):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartamentoSerializers(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # De nuevo, evalúa si quieres permitir eliminar departamentos
    def delete(self, request, pk):
        try:
            departamento = Departamento.objects.get(pk=pk)
        except Departamento.DoesNotExist:
            return Response({'error': 'Departamento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        departamento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
