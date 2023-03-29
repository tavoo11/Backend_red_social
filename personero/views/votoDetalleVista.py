from rest_framework import generics
from personero.serializers.votoSerializer import VotoSerializer
from personero.modelos.voto import Voto
from rest_framework.response import Response
from rest_framework import  status

class VotoDetalleVista(generics.ListCreateAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

    def get(self, request, *args, **kwargs):
        votos = self.get_queryset()
        serializer = VotoSerializer(votos, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        voto = self.get_object()
        serializer = VotoSerializer(voto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        voto = self.get_object()
        voto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
