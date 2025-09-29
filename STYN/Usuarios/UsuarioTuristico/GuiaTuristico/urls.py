# en UsuarioTuristico/urls.py
from django.urls import path
from Usuarios.UsuarioTuristico.GuiaTuristico.ApiView import GuiaTuristicoCreateView

urlpatterns = [
    # … tus otras urls
    path('registro/', GuiaTuristicoCreateView.as_view(), name='guia-registro'),
]
