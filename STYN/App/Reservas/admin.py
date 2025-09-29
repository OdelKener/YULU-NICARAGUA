# App/Reservas/admin.py
from django.contrib import admin
from .models import Reserva, ServicioComplementario, ServicioReserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'usuario', 'guia', 'sitio',
        'fecha_reserva', 'hora_inicio', 'estado',
        'numero_personas', 'precio_total', 'comision_plataforma'
    )
    list_filter = ('estado', 'metodo_pago', 'fecha_reserva')
    search_fields = ('usuario__name', 'guia__usuario__name', 'sitio__nombre', 'codigo_confirmacion')
    readonly_fields = ('fecha_creacion', 'codigo_confirmacion', 'precio_total', 'comision_plataforma')
    ordering = ('-fecha_creacion',)


@admin.register(ServicioComplementario)
class ServicioComplementarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'precio', 'disponible')
    list_filter = ('tipo', 'disponible')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)


@admin.register(ServicioReserva)
class ServicioReservaAdmin(admin.ModelAdmin):
    list_display = ('id', 'reserva', 'servicio', 'cantidad', 'precio_unitario', 'subtotal')
    search_fields = ('reserva__usuario__name', 'servicio__nombre')
    ordering = ('reserva',)
