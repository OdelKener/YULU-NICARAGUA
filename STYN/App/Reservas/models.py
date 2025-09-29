# App/Reservas/models.py
from django.db import models
from Usuarios.UsuarioGuia.models import GuiaTuristico
from Usuarios.UsuarioTuristico.models import UsuarioTuristico
from App.SitiosTuristicos.models import SitiosTuristicos


class Reserva(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    METODOS_PAGO = [
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta Crédito/Débito'),
        ('transferencia', 'Transferencia'),
        ('paypal', 'PayPal'),
    ]

    usuario = models.ForeignKey(UsuarioTuristico, on_delete=models.CASCADE, related_name='reservas')
    guia = models.ForeignKey(GuiaTuristico, on_delete=models.CASCADE, related_name='reservas')
    sitio = models.ForeignKey(SitiosTuristicos, on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    duracion_horas = models.IntegerField(default=4)

    numero_personas = models.IntegerField(default=1)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comision_plataforma = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO, blank=True)

    requisitos_especiales = models.TextField(blank=True)
    punto_encuentro = models.CharField(max_length=200, blank=True)

    codigo_confirmacion = models.CharField(max_length=6, blank=True)
    calificacion = models.IntegerField(null=True, blank=True)
    comentario = models.TextField(blank=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return f"Reserva #{self.id} - {self.usuario.name} con {self.guia.usuario.name}"


class ServicioComplementario(models.Model):
    TIPOS_SERVICIO = [
        ('transporte', 'Transporte'),
        ('alimentacion', 'Alimentación'),
        ('equipo', 'Equipo Especializado'),
        ('alojamiento', 'Alojamiento'),
        ('seguro', 'Seguro de Viaje'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_SERVICIO)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"


class ServicioReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='servicios_adicionales')
    servicio = models.ForeignKey(ServicioComplementario, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ['reserva', 'servicio']

    def subtotal(self):
        return self.cantidad * self.precio_unitario


