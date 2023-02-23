from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from appCitas.serializars.usuarioSerializer import UsuarioSerializer

class UsuarioCrearVista(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {'username': request.data['username'], 'password': request.data['password']}
        tokenSerializer = TokenObtainPairSerializer(data= tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)