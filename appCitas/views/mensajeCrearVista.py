from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views, status
from rest_framework.response import Response


from appCitas.serializars.mensajeSerializer import MensajeSerializer

class MensajeCrearVista(views.APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        data = request.data.copy()  # hacer una copia del objeto de datos
        data['usuario'] = request.user.id  # agregar el ID del usuario actual al objeto de datos
        serializer = MensajeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


