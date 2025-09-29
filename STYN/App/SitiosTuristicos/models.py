from django.db import models
from App.Departamento.models import Departamento

class SitiosTuristicos(models.Model):
    TIPO_CHOICES = [
        ('playa', 'Playa'),
        ('ciudad_patrimonial', 'Ciudad Patrimonial'),
        ('hospedaje', 'Hospedaje'),
        ('reserva_natural', 'Reserva Natural'),
        # Se pueden agregar más: volcan, lago, etc.
    ]

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    direccion = models.TextField(blank=True)  # Útil para hospedajes/ciudades
    latitud = models.FloatField(null=True, blank=True)  # Para mapas
    longitud = models.FloatField(null=True, blank=True)  # Para mapas
    precio_aprox = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Para hospedajes

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})"

