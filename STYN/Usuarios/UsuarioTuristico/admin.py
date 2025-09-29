from django.contrib import admin
from . models import UsuarioTuristico

@admin.register(UsuarioTuristico)
class UsuarioTuristicoAdmin(admin.ModelAdmin):
    search_fields = ['id',"name"]
    list_display = ["id","name","lastname","sexo","email", "pais"]