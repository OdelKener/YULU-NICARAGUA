from django.contrib import admin
from . models import EventosTuristicos
from .models import Departamento

@admin.register(EventosTuristicos)
class LibroAdmin(admin.ModelAdmin):
    search_fields = ['nombre','departamento']
    list_display = ["nombre",  "departamento", "descripcion", "mes"]