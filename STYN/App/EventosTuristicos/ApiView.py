# App/EventosTuristicos/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .models import EventosTuristicos
from .serializers import EventosTuristicosSerializers


class EventoTuristicoApiView(APIView):

    @swagger_auto_schema(responses={200: EventosTuristicosSerializers(many=True)})
    def get(self, request):
        eventos = EventosTuristicos.objects.all()
        serializer = EventosTuristicosSerializers(eventos, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EventosTuristicosSerializers, responses={201:EventosTuristicosSerializers})
    def post(self, request):
        serializer = EventosTuristicosSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventoTuristicoDetailView(APIView):

    @swagger_auto_schema(responses={200: EventosTuristicosSerializers})
    def get(self, request, pk):
        try:
            evento = EventosTuristicos.objects.get(pk=pk)
        except EventosTuristicos.DoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer =EventosTuristicosSerializers(evento)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=EventosTuristicosSerializers, responses={200:EventosTuristicosSerializers})
    def put(self, request, pk):
        try:
            evento = EventosTuristicos.objects.get(pk=pk)
        except EventosTuristicos.DoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventosTuristicosSerializers(evento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            evento = EventosTuristicos.objects.get(pk=pk)
        except EventosTuristicos.DoesNotExist:
            return Response({'error': 'Evento no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        evento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
