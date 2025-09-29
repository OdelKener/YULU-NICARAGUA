from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Userabs
from Usuarios.UsuarioTuristico.models import UsuarioTuristico


class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = Userabs
        fields = ['username', 'email', 'password', 'password_confirm', 'tipo_usuario', 'first_name', 'last_name',
                  'telefono']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        # Verificar que el email no exista en UsuarioTuristico
        if UsuarioTuristico.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Este email ya está registrado")

        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)

        user = Userabs.objects.create(**validated_data)

        # Crear el perfil correspondiente según el tipo
        if validated_data['tipo_usuario'] == 'turista':
            self.crear_usuario_turistico(user)
        elif validated_data['tipo_usuario'] == 'guia':
            self.crear_guia_turistico(user)

        return user

    def crear_usuario_turistico(self, user):
        """Crear perfil en UsuarioTuristico cuando se registra como turista"""
        UsuarioTuristico.objects.create(
            name=user.first_name,
            lastname=user.last_name,
            sexo='M',  # Por defecto, luego puede editar
            email=user.email,
            pais='NI'  # Por defecto Nicaragua
        )

    def crear_guia_turistico(self, user):
        """Solo crear usuario base, el guía debe completar perfil después"""
        UsuarioTuristico.objects.create(
            name=user.first_name,
            lastname=user.last_name,
            sexo='M',
            email=user.email,
            pais='NI'
        )
        # El perfil de GuiaTuristico lo completará después con documentación


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()  # email o username
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Buscar usuario
        try:
            user = Userabs.objects.get(email=email)
        except Userabs.DoesNotExist:
            try:
                user = Userabs.objects.get(username=email)
            except Userabs.DoesNotExist:
                raise serializers.ValidationError("Usuario no encontrado")

        # Verificar contraseña
        if not user.check_password(password):
            raise serializers.ValidationError("Contraseña incorrecta")
        if not user.is_active:
            raise serializers.ValidationError("Cuenta desactivada")

        data['user'] = user
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userabs
        fields = ['id', 'username', 'email', 'tipo_usuario', 'first_name', 'last_name', 'telefono']
