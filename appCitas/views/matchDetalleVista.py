from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import views, status
from rest_framework.response import Response

from appCitas.models.match import Match
from appCitas.serializars.matchSerializer import MatchSerializer

class MatchDetalleVista(views.APIView):
    authentication_classes = [JWTAuthentication]
    http_method_names = ['get', 'put', 'delete']

    def get(self, request, pk=None):
        if pk:
            matc = Match.objects.get(pk=pk)
            serializer = MatchSerializer(matc)
            return Response(serializer.data)
        else:
            matches = Match.objects.all()
            serializer = MatchSerializer(matches)
            return Response(serializer.data)

    def put(self, request, pk= None):
        matche = Match.objects.get(pk=pk)
        serializer = MatchSerializer(matche, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk=None):
        matche = Match.objects.get(pk=pk)
        matche.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)