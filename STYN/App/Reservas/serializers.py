# App/Reservas/serializers.py
from django.db.models import DecimalField
from rest_framework import serializers
from .models import Reserva, ServicioComplementario, ServicioReserva
from Usuarios.UsuarioGuia.models import GuiaTuristico
from Usuarios.UsuarioGuia.serializers import GuiaTuristicoRegisterSerializer
from Usuarios.UsuarioTuristico.serializers import UsuarioTuristicoSerilizers
from App.SitiosTuristicos.serializers import SitiosTuristicosSerializers
from django.utils import timezone
from decimal import Decimal


class ServicioComplementarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioComplementario
        fields = '__all__'


class ServicioReservaSerializer(serializers.ModelSerializer):
    servicio_info = ServicioComplementarioSerializer(source='servicio', read_only=True)

    class Meta:
        model = ServicioReserva
        fields = '__all__'
        extra_kwargs = {'servicio': {'write_only': True}}


class ReservaSerializer(serializers.ModelSerializer):
    usuario_info = UsuarioTuristicoSerilizers(source='usuario', read_only=True)
    guia_info = GuiaTuristicoRegisterSerializer(source='guia', read_only=True)
    sitio_info = SitiosTuristicosSerializers(source='sitio', read_only=True)
    servicios = ServicioReservaSerializer(source="servicios_adicionales", many=True, read_only=True)

    # 🔒 Solo guías aprobados pueden ser seleccionados
    guia = serializers.PrimaryKeyRelatedField(
        queryset=GuiaTuristico.objects.filter(aprobado=True),
        write_only=True
    )

    class Meta:
        model = Reserva
        fields = '__all__'
        extra_kwargs = {
            'usuario': {'write_only': True},
            'sitio': {'write_only': True},
        }

    def validate(self, data):
        # Validar fecha futura
        if data['fecha_reserva'] < timezone.now().date():
            raise serializers.ValidationError("La fecha de reserva debe ser futura")

        # Validar disponibilidad del guía
        reservas_existentes = Reserva.objects.filter(
            guia=data['guia'],
            fecha_reserva=data['fecha_reserva'],
            estado__in=['pendiente', 'confirmada', 'en_progreso']
        )
        if reservas_existentes.exists():
            raise serializers.ValidationError("El guía ya tiene una reserva en esa fecha")

        return data

    def create(self, validated_data):
        # Calcular precio total automáticamente
        guia = validated_data['guia']
        horas = validated_data.get('duracion_horas', 4)
        personas = validated_data.get('numero_personas', 1)

        validated_data['precio_total'] = guia.precio_por_hora * horas * personas
        validated_data['comision_plataforma'] = validated_data['precio_total'] * Decimal('0.10')

        return super().create(validated_data)
