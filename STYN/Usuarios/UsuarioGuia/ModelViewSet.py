from rest_framework import viewsets
from .models import GuiaTuristico
from .serializers import GuiaTuristicoRegisterSerializer
from rest_framework.permissions import IsAuthenticated


from rest_framework import viewsets
from .models import GuiaTuristico
from .serializers import GuiaTuristicoRegisterSerializer, GuiaTuristicoListSerializer
from rest_framework.permissions import IsAuthenticated

class GuiaTuristicoViewSet(viewsets.ModelViewSet):
    queryset = GuiaTuristico.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return GuiaTuristicoListSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        aprobado = self.request.query_params.get('estado')
        qs = super().get_queryset()
        if aprobado == 'aprobado':
            qs = qs.filter(aprobado=True)
        return qs
