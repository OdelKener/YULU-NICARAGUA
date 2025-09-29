# App/Reservas/views.py
# App/Reservas/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.core.mail import send_mail
from django.conf import settings
import random, string
from decimal import Decimal
import random
import string
from .models import Reserva, ServicioComplementario
from .serializers import ReservaSerializer, ServicioComplementarioSerializer
from Usuarios.UsuarioTuristico.models import UsuarioTuristico
from Usuarios.UsuarioGuia.models import GuiaTuristico


class ReservaApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            usuario_turistico = UsuarioTuristico.objects.get(email=request.user.email)
        except UsuarioTuristico.DoesNotExist:
            return Response({"error": "Debes registrarte como Usuario Turístico"}, status=400)

        reservas = Reserva.objects.filter(usuario=usuario_turistico)
        serializer = ReservaSerializer(reservas, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ReservaSerializer, responses={201: ReservaSerializer})
    def post(self, request):
        try:
            usuario_turistico = UsuarioTuristico.objects.get(email=request.user.email)
        except UsuarioTuristico.DoesNotExist:
            return Response({"error": "Debes registrarte como Usuario Turístico"}, status=400)

        data = request.data.copy()
        data['usuario'] = usuario_turistico.id

        # Validar guía aprobado
        try:
            guia = GuiaTuristico.objects.get(id=data['guia'], aprobado=True)
        except GuiaTuristico.DoesNotExist:
            return Response({"error": "El guía no existe o no está aprobado"}, status=400)

        # Generar código confirmación
        data['codigo_confirmacion'] = ''.join(random.choices(string.digits, k=6))

        serializer = ReservaSerializer(data=data)
        if serializer.is_valid():
            reserva = serializer.save()

            # Calcular precio y comisión
            reserva.precio_total = guia.precio_por_hora * reserva.duracion_horas * reserva.numero_personas
            reserva.comision_plataforma = reserva.precio_total * Decimal('0.10')  # Decimal en vez de float
            reserva.save()

            # Intentar enviar correo, pero no romper la reserva si falla
            try:
                self.enviar_confirmacion(reserva)
            except Exception as e:
                print(f"Error enviando correo: {e}")  # en dev, solo lo imprime
                # Puedes agregar logging aquí para producción

            return Response({
                'reserva': ReservaSerializer(reserva).data,
                'mensaje': 'Reserva creada. Proceda al pago.',
                'codigo_confirmacion': reserva.codigo_confirmacion
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def enviar_confirmacion(self, reserva):
        asunto = "Nueva reserva creada"
        mensaje = (
            f"Hola {reserva.usuario.name},\n\n"
            f"Tu reserva con el guía {reserva.guia.usuario.name} ha sido creada.\n"
            f"Código de confirmación: {reserva.codigo_confirmacion}\n"
            f"Precio total: ${reserva.precio_total}\n\n"
            f"Punto de encuentro: {reserva.punto_encuentro or 'Por definir'}\n\n"
            f"Gracias por usar nuestra plataforma."
        )
        destinatarios = [reserva.usuario.email, reserva.guia.usuario.email]

        send_mail(asunto, mensaje, settings.DEFAULT_FROM_EMAIL, destinatarios)



class ConfirmarReservaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, reserva_id):
        try:
            usuario_turistico = UsuarioTuristico.objects.get(email=request.user.email)
            reserva = Reserva.objects.get(id=reserva_id, usuario=usuario_turistico)
        except (UsuarioTuristico.DoesNotExist, Reserva.DoesNotExist):
            return Response({'error': 'Reserva no encontrada'}, status=404)

        codigo = request.data.get('codigo_confirmacion')
        if reserva.codigo_confirmacion == codigo:
            reserva.estado = 'confirmada'
            reserva.save()
            return Response({'mensaje': 'Reserva confirmada exitosamente'})
        else:
            return Response({'error': 'Código de confirmación inválido'}, status=400)


class ServiciosComplementariosView(APIView):
    @swagger_auto_schema(responses={200: ServicioComplementarioSerializer(many=True)})
    def get(self, request):
        servicios = ServicioComplementario.objects.filter(disponible=True)
        serializer = ServicioComplementarioSerializer(servicios, many=True)
        return Response(serializer.data)
