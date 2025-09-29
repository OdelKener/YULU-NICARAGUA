from django.db import models
from App.Departamento.models import Departamento

class EventosTuristicos(models.Model):
    MESES_CHOICES = [
        (1, 'Enero'),
        (2, 'Febrero'),
        (3, 'Marzo'),
        (4, 'Abril'),
        (5, 'Mayo'),
        (6, 'Junio'),
        (7, 'Julio'),
        (8, 'Agosto'),
        (9, 'Septiembre'),
        (10, 'Octubre'),
        (11, 'Noviembre'),
        (12, 'Diciembre'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    mes = models.IntegerField(choices=MESES_CHOICES)  # clave: controlás en qué mes ocurre

    class Meta:
        ordering = ['mes', 'departamento__nombre']

    def __str__(self):
        return f"{self.nombre} - {self.get_mes_display()} ({self.departamento.nombre})"


