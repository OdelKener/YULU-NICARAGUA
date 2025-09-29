from django.urls import path, include

urlpatterns=[

path('UsuarioGuia/', include('Usuarios.UsuarioGuia.urls')),
path('EventosTuristicos/', include('App.Reservas.urls')),
path('UsuarioTuristico/', include('Usuarios.UsuarioTuristico.urls')),
path('Auth/', include('Usuarios.Auth.urls')),

]
