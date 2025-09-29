from rest_framework.serializers import ModelSerializer
from .models import EventosTuristicos

class EventosTuristicosSerializers(ModelSerializer):
    class Meta:
        model = EventosTuristicos
        fields = ["nombre", "descripcion", "departamento", "mes"]
