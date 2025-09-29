from django.db import models
from django_countries.fields import CountryField


class UsuarioTuristico(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=100)
    lastname = models.CharField(verbose_name='Apellido', max_length=100)
    sexo = models.CharField(
        verbose_name='Sexo',
        max_length=1,
        choices=[('M', 'Masculino'), ('F', 'Femenino')]
    )
    email = models.EmailField(verbose_name='Correo electrónico', unique=True)
    pais = CountryField(blank_label='(selecciona país)')

    class Meta:
        verbose_name = "Usuario Turístico"
        verbose_name_plural = "Usuarios Turísticos"

    def __str__(self):
        return f"{self.name} {self.lastname} - {self.pais.name}"