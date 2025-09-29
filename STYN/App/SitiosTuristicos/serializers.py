from rest_framework import serializers
from .models import SitiosTuristicos

class SitiosTuristicosSerializers(serializers.ModelSerializer):
    class Meta:
        model = SitiosTuristicos
        fields = ["id", "nombre", "tipo", "departamento", "descripcion", "direccion", "latitud", "longitud", "precio_aprox"]

