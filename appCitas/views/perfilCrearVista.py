from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views, status
from appCitas.serializars.perfilSerializer import PerfilSerializer
from rest_framework.response import Response

class PerfilCrearView(views.APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = PerfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)