from rest_framework import viewsets
from .models import EventosTuristicos
from .serializers import EventosTuristicosSerializers

class EventosTuristicosViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint para ver eventos turísticos (solo lectura).
    """
    queryset = EventosTuristicos.objects.all()
    serializer_class = EventosTuristicosSerializers
