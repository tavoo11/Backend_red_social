from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views
from appCitas.models.perfil import Perfil
from appCitas.models.usuario import Usuario
from appCitas.serializars.perfilSerializer import PerfilSerializer
from rest_framework.response import Response

class PerfilObtenerView(views.APIView):
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, pk=None):
        perfiles = Perfil.objects.all()
        serializer = PerfilSerializer(perfiles, many=True)
        return Response(serializer.data) 