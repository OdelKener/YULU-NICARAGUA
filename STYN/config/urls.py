
# from django.contrib import admin
# # from django.urls import path, include
# #
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="API con autenticación JWT",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #
    # # JWT Token endpoints
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Rutas de tus apps
    path('Usuarios/', include('Usuarios.urls')),
    path('Departamento/', include('App.Departamento.urls')),
    path('SitiosTuristicos/', include('App.SitiosTuristicos.urls')),
    path('Reservas/', include('App.Reservas.urls')),
    path('EventosTuristicos/', include('App.EventosTuristicos.urls')),
    # path('Auth/', include('Usuarios..urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
