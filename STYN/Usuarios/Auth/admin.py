from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Userabs


@admin.register(Userabs)
class UserAdmin(BaseUserAdmin):
    # Campos de búsqueda
    search_fields = ['username', 'email', 'first_name', 'last_name', 'telefono']

    # Campos a mostrar en la lista
    list_display = ['username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'telefono', 'is_active', 'is_staff',
                    'date_joined']

    # Filtros laterales
    list_filter = ['tipo_usuario', 'is_active', 'is_staff', 'is_superuser', 'date_joined']

    # Campos de solo lectura
    readonly_fields = ['date_joined', 'last_login']

    # Ordenamiento por defecto
    ordering = ['-date_joined']

    # Campos para búsqueda jerárquica
    list_select_related = True

    # Acciones personalizadas
    actions = ['activar_usuarios', 'desactivar_usuarios']

    # Configuración de campos para edición
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email', 'telefono')
        }),
        ('Tipo de Usuario', {
            'fields': ('tipo_usuario',)
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Fechas Importantes', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )

    # Configuración para agregar usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'email', 'password1', 'password2', 'tipo_usuario', 'first_name', 'last_name', 'telefono'),
        }),
    )

    def activar_usuarios(self, request, queryset):
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} usuarios activados exitosamente.')

    activar_usuarios.short_description = "Activar usuarios seleccionados"

    def desactivar_usuarios(self, request, queryset):
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} usuarios desactivados exitosamente.')

    desactivar_usuarios.short_description = "Desactivar usuarios seleccionados"