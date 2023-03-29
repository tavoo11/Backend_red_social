from rest_framework import generics
from personero.serializers.candidatoSerializer import CandidatoSerializer
from personero.modelos.candidato import Candidato

class CandidatoCrearVista(generics.CreateAPIView):
    serializer_class = CandidatoSerializer
    queryset = Candidato.objects.all()