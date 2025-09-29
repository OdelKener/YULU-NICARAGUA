from  rest_framework.serializers import  ModelSerializer
from Usuarios.UsuarioTuristico.models import UsuarioTuristico

class UsuarioTuristicoSerilizers(ModelSerializer):
    class Meta:
        model = UsuarioTuristico
        fields = ["name","lastname","sexo","email", "pais"]
