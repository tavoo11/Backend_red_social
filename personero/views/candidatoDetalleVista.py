from rest_framework import generics
from personero.serializers.candidatoSerializer import CandidatoSerializer
from personero.modelos.candidato import Candidato
from rest_framework.response import Response
from rest_framework import  status

class CandidatoDetalleVista(generics.CreateAPIView):
    serializer_class = CandidatoSerializer
    queryset = Candidato.objects.all()

    def get(self, request, *args, **kwargs):
        candidatos = self.get_queryset()
        serializer = CandidatoSerializer(candidatos, many=True)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        candidato = self.get_object()
        serializer = CandidatoSerializer(candidato, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        candidato = self.get_object()
        candidato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
