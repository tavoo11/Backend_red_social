from rest_framework import views, status
from rest_framework.response import Response
from appCitas.models.usuario import Usuario
from appCitas.models.perfil import Perfil
from appCitas.models.match import Match
from appCitas.serializars.matchSerializer import MatchSerializer
from appCitas.serializars.usuarioSerializer import UsuarioSerializer

class UsuarioDetalleVista(views.APIView):
    http_method_names = ['get', 'put', 'delete']
    def get(self, request, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(pk=kwargs['pk'])
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)
        except Usuario.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, pk):
        usuario = Usuario.objects.get(pk=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
