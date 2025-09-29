from django.contrib import admin
from . models import SitiosTuristicos
from .models import Departamento

@admin.register(SitiosTuristicos)
class LibroAdmin(admin.ModelAdmin):
    search_fields = ['nombre','tipo']
    list_display = ["nombre", "tipo", "departamento", "descripcion", "direccion", "latitud", "longitud", "precio_aprox"]