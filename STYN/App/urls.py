from django.urls import path, include

urlpatterns=[

path('Departamento/', include('App.Departamento.urls')),
path('SitiosTuristicos/', include('App.SitiosTuristicos.urls')),
path('EventosTuristicos/', include('App.EventosTuristicos.urls')),
path('Reservas/', include('App.Reservas.urls')),






]
