from rest_framework import viewsets
from .models import Departamento
from .serializers import DepartamentoSerializers

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializers
