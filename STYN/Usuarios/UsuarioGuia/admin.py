from django.contrib import admin
from . models import GuiaTuristico


# App/Usuarios/admin.py
@admin.register(GuiaTuristico)
class GuiaTuristicoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cedula', 'aprobado', 'fecha_registro', 'esta_completo')
    list_filter = ('aprobado', 'zonas_cobertura', 'sexo')
    search_fields = ('usuario__name', 'usuario__lastname', 'cedula')
    readonly_fields = ('fecha_registro', 'fecha_aprobacion')

    actions = ['aprobar_guias', 'rechazar_guias']

    def aprobar_guias(self, request, queryset):
        queryset.update(aprobado=True)
        self.message_user(request, f"{queryset.count()} guías aprobados")

    aprobar_guias.short_description = "Aprobar guías seleccionados"

    def rechazar_guias(self, request, queryset):
        queryset.update(aprobado=False)
        self.message_user(request, f"{queryset.count()} guías rechazados")