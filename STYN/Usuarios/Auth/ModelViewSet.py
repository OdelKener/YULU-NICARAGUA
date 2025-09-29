from rest_framework import viewsets
from .models import Userabs
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = Userabs.objects.all()
    serializer_class = UserSerializer
