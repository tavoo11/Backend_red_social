from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views, status
from rest_framework.response import Response

from appCitas.serializars.mensajeSerializer import MensajeSerializer
from appCitas.models.mensaje import Mensaje

class MensajeDetalleVista(views.APIView):
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, pk= None):
        if pk:
            mensaje = Mensaje.objects.get(pk=pk)
            serializer = MensajeSerializer(mensaje)
            return Response(serializer.data) 
        else:
            mensajes = Mensaje.objects.all()
            serializer = MensajeSerializer(mensajes)
            return Response(serializer.data)
    

    def delete(self, pk):
        mensaje = Mensaje.objects.get(pk=pk)
        mensaje.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
