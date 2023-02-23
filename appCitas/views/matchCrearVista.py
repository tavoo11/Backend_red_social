from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views, status
from rest_framework.response import Response

from appCitas.serializars import MatchSerializer

class MatchCrearVista (views.APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)