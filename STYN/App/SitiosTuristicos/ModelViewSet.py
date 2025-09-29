from rest_framework import viewsets
from .models import SitiosTuristicos
from .serializers import SitiosTuristicosSerializers

class SitiosTuristicosViewSet(viewsets.ModelViewSet):
    queryset = SitiosTuristicos.objects.all()
    serializer_class = SitiosTuristicosSerializers
