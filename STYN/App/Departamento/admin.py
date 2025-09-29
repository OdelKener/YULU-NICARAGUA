from django.contrib import admin
from . models import Departamento

@admin.register(Departamento)
class LibroAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ["nombre"]
