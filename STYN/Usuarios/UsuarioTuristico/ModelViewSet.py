from rest_framework import viewsets
from .models import UsuarioTuristico
from .serializers import UsuarioTuristicoSerilizers

class UsuarioTuristicoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioTuristico.objects.all()
    serializer_class = UsuarioTuristicoSerilizers
