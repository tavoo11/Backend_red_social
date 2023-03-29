from personero.modelos.candidato import Candidato
from rest_framework import serializers

class CandidatoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Candidato
        fields = '__all__'