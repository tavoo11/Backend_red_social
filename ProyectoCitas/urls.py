
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from appCitas.views.usuarioCrearVista import UsuarioCrearVista
from appCitas.views.usuarioDetalleVista import UsuarioDetalleVista
from appCitas.views.perfilCrearVista import PerfilCrearView
from appCitas.views.perfilDetalleVista import PerfilObtenerView
from appCitas.views.matchCrearVista import MatchCrearVista
from appCitas.views.matchDetalleVista import MatchDetalleVista
from appCitas.views.mensajeCrearVista import MensajeCrearVista
from appCitas.views.mensajeDetalleVista import MensajeDetalleVista

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('usuario/', UsuarioCrearVista.as_view()),
    path('usuarioid/<int:pk>', UsuarioDetalleVista.as_view(), name='usuario especifico'),
    path('usuarioid/', UsuarioDetalleVista.as_view(), name='usarios todos'),
    path('perfil/', PerfilCrearView.as_view()),
    path('perfilid/<int:pk>', PerfilObtenerView.as_view()),
    path('perfilid/', PerfilObtenerView.as_view()),
    path('match/', MatchCrearVista.as_view()),
    path('matchid/<int:pk>', MatchDetalleVista.as_view()),
    path('mensaje/', MensajeCrearVista.as_view()),
    path('mensaje/<int:id_emisor>/<int:id_receptor>/', MensajeDetalleVista.as_view()),
    path('mensaje/', MensajeDetalleVista.as_view()),


] 