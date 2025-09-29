# App/views.py
from django.shortcuts import render

def sitios_turisticos(request):
    return render(request, 'sitios_turisticos.html')
