from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views, status
from rest_framework.response import Response

from appCitas.serializars.mensajeSerializer import MensajeSerializer
from appCitas.models.mensaje import Mensaje

class MensajeDetalleVista(views.APIView):
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        id_emisor = kwargs.get('id_emisor')
        id_receptor = kwargs.get('id_receptor')
        print(id_emisor, id_receptor)
        if id_emisor and id_receptor:
            try:
                mensajes = Mensaje.objects.filter(
                    id_emisor=id_emisor, id_receptor=id_receptor
                )
                serializer = MensajeSerializer(mensajes, many=True)
                return Response(serializer.data)
            except Mensaje.DoesNotExist:
                Response(status=status.HTTP_404_NOT_FOUND)
        else:
            mensajes = Mensaje.objects.all()
            serializer = MensajeSerializer(mensajes, many=True)
            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id_emisor = request.GET.get('pk')
        id_receptor = request.GET.get('id_receptor')
        if id_emisor and id_receptor:
            mensajes = Mensaje.objects.filter(
                id_emisor=id_emisor, id_receptor=id_receptor
            )
            mensajes.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)