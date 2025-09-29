from django.urls import path
from .ApiView  import RegistroView, LoginView, LogoutView, PerfilView, RegistroTemplateView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='auth-registro'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
    path('perfil/', PerfilView.as_view(), name='auth-perfil'),
    path('registro-page/', RegistroTemplateView.as_view(), name='registro-page'),  # Template
]
