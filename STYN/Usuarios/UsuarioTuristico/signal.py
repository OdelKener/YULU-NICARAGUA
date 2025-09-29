# App/Usuarios/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UsuarioTuristico

@receiver(post_save, sender=User)
def crear_usuario_turistico(sender, instance, created, **kwargs):
    if created:
        UsuarioTuristico.objects.create(
            user=instance,
            name=instance.first_name,
            lastname=instance.last_name,
            email=instance.email,
            sexo='M',  # valor por defecto, luego se edita
            pais='NI'  # valor por defecto
        )
