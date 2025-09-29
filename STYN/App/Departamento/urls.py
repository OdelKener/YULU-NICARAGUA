from django.urls import  path, include
from rest_framework.routers import  DefaultRouter
from .ApiView import DepartamentoApiView
from .ModelViewSet import DepartamentoViewSet
from .models import Departamento

router = DefaultRouter()
router.register(r'departamento',DepartamentoViewSet, basename='departamento')

urlpatterns = [

    path('', include(router.urls)),

]
