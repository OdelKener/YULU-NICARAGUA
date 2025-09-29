# App/SitiosTuristicos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import SitiosTuristicos
from .serializers import SitiosTuristicosSerializers  # Usaremos el serializer mejorado

class SitiosTuristicosApiView(APIView):

    @swagger_auto_schema(responses={200: SitiosTuristicosSerializers(many=True)})
    def get(self, request):
        sitiosturisticos = SitiosTuristicos.objects.all()
        serializer = SitiosTuristicosSerializers(sitiosturisticos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SitiosTuristicosSerializers, responses={201: SitiosTuristicosSerializers})
    def post(self, request):
        serializer = SitiosTuristicosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SitiosTuristicosDetailView(APIView):

    @swagger_auto_schema(responses={200: SitiosTuristicosSerializers})
    def get(self, request, pk):
        try:
            sitioturistico = SitiosTuristicos.objects.get(pk=pk)
        except SitiosTuristicos.DoesNotExist:
            return Response({'error': 'Sitio turístico no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SitiosTuristicosSerializers(sitioturistico)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=SitiosTuristicosSerializers, responses={200: SitiosTuristicosSerializers})
    def put(self, request, pk):
        try:
            sitioturistico = SitiosTuristicos.objects.get(pk=pk)
        except SitiosTuristicos.DoesNotExist:
            return Response({'error': 'Sitio turístico no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SitiosTuristicosSerializers(sitioturistico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            sitioturistico = SitiosTuristicos.objects.get(pk=pk)
        except SitiosTuristicos.DoesNotExist:
            return Response({'error': 'Sitio turístico no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        sitioturistico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
