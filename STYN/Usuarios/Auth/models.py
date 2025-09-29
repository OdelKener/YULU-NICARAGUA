from django.db import models
from django.contrib.auth.models import AbstractUser

class Userabs(AbstractUser):
    TIPO_USUARIO = [
        ('turista', 'Turista'),
        ('guia', 'Guía'),
        ('admin', 'Administrador'),
    ]

    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO, default='turista')
    telefono = models.CharField(max_length=15, blank=True)

    # Agrega related_name personalizados para evitar conflictos
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='auth_user_set',  # Cambia este related_name
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='auth_user_set',  # Cambia este related_name
        related_query_name='user',
    )

    def __str__(self):
        return f"{self.username} ({self.email})"