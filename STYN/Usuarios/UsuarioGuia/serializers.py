from rest_framework import serializers
from Usuarios.UsuarioGuia.models import GuiaTuristico

class GuiaTuristicoRegisterSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='usuario.name', read_only=True)
    apellido = serializers.CharField(source='usuario.lastname', read_only=True)

    class Meta:
        model = GuiaTuristico
        fields = [
            'id',                 # para el value del <option>
            'nombre', 'apellido', # 👈 ya tienes nombre y apellido en JSON
            'usuario','sexo', 'cedula', 'foto_cedula_frontal', 'foto_cedula_reverso',
            'certificado_guia', 'licencia_conducir', 'idiomas', 'especialidades',
            'experiencia', 'anos_experiencia', 'precio_por_hora', 'precio_por_dia',
            'zonas_cobertura', 'telefono_whatsapp', 'enlace_facebook', 'enlace_instagram'
        ]
        extra_kwargs = {
            'usuario': {'read_only': True}  # ← esto evita el error
        }

    def validate_cedula(self, value):
        if len(value) not in [4, 15]:
            raise serializers.ValidationError("La cédula debe tener 4 o 16 caracteres")
        return value

class GuiaTuristicoListSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='usuario.name', read_only=True)
    apellido = serializers.CharField(source='usuario.lastname', read_only=True)

    class Meta:
        model = GuiaTuristico
        fields = ['id', 'nombre', 'apellido']

