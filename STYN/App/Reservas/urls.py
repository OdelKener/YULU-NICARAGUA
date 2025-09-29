# App/Reservas/urls.py
from django.urls import path
from .ApiView import ReservaApiView, ConfirmarReservaView, ServiciosComplementariosView

urlpatterns = [
    path('reservas/', ReservaApiView.as_view(), name='reservas-list'),
    path('reservas/<int:reserva_id>/confirmar/', ConfirmarReservaView.as_view(), name='confirmar-reserva'),
    path('servicios-complementarios/', ServiciosComplementariosView.as_view(), name='servicios-complementarios'),
]
