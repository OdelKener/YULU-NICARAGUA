from django.db import models
import os


def upload_to_certificaciones(instance, filename):
    # Guardar en: certificaciones/guia_{id}/{filename}
    return os.path.join('certificaciones', f'guia_{instance.usuario.id}', filename)


def upload_to_identificacion(instance, filename):
    return os.path.join('identificaciones', f'guia_{instance.usuario.id}', filename)


class GuiaTuristico(models.Model):
    # Relación con usuario
    usuario = models.OneToOneField(
        'UsuarioTuristico.UsuarioTuristico',
        on_delete=models.CASCADE,
        related_name="perfil_guia"
    )

    # Información básica
    sexo = models.CharField(
        verbose_name='Sexo',
        max_length=1,
        choices=[('M', 'Masculino'), ('F', 'Femenino')]
    )
    cedula = models.CharField(verbose_name='Cédula', max_length=16, unique=True)

    # Documentación OBLIGATORIA
    foto_cedula_frontal = models.ImageField(
        upload_to=upload_to_identificacion,
        verbose_name='Foto Cédula Frontal'
    )
    foto_cedula_reverso = models.ImageField(
        upload_to=upload_to_identificacion,
        verbose_name='Foto Cédula Reverso'
    )
    certificado_guia = models.FileField(
        upload_to=upload_to_certificaciones,
        verbose_name='Certificado de Guía Turístico',
        blank=True,
        null=True
    )
    licencia_conducir = models.FileField(
        upload_to=upload_to_certificaciones,
        verbose_name='Licencia de Conducir (opcional)',
        blank=True,
        null=True
    )

    # Información profesional
    idiomas = models.CharField(
        max_length=100,
        help_text="Ej: Español, Inglés, Francés. Separados por comas"
    )
    especialidades = models.CharField(
        max_length=200,
        help_text="Ej: Avistamiento de aves, Historia colonial, Surf, etc.",
        blank=True
    )
    experiencia = models.TextField(
        verbose_name='Experiencia y formación',
        help_text="Describe tu experiencia como guía, estudios relacionados, etc."
    )
    anos_experiencia = models.IntegerField(
        verbose_name='Años de experiencia',
        default=0
    )

    # Información de servicios
    precio_por_hora = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio por hora (USD)',
        default=20.00
    )
    precio_por_dia = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio por día completo (USD)',
        default=100.00
    )
    zonas_cobertura = models.CharField(
        max_length=300,
        help_text="Departamentos o ciudades donde trabajas. Ej: Granada, Masaya, Ometepe",
        default='Granada'
    )

    # Estado y validación
    aprobado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_aprobacion = models.DateTimeField(null=True, blank=True)

    # Métodos de contacto
    telefono_whatsapp = models.CharField(max_length=15, blank=True)
    enlace_facebook = models.URLField(blank=True)
    enlace_instagram = models.URLField(blank=True)

    class Meta:
        verbose_name = "Guía Turístico"
        verbose_name_plural = "Guías Turísticos"
        ordering = ['-fecha_registro']

    def save(self, *args, **kwargs):
        # Validar que el usuario sea nicaragüense
        if self.usuario.pais.code != "NI":
            raise ValueError("Solo usuarios nicaragüenses pueden registrarse como guías.")

        # Si es aprobado por primera vez, registrar fecha
        if self.aprobado and not self.fecha_aprobacion:
            from django.utils import timezone
            self.fecha_aprobacion = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Guía: {self.usuario.name} {self.usuario.lastname} - Cédula: {self.cedula}"

    @property
    def esta_completo(self):
        """Verifica si el perfil está completo para revisión"""
        return all([
            self.foto_cedula_frontal,
            self.foto_cedula_reverso,
            self.experiencia.strip(),
            self.idiomas.strip(),
            self.zonas_cobertura.strip()
        ])
