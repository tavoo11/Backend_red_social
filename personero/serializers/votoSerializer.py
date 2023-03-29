from personero.modelos.candidato import Candidato
from personero.modelos.estudiante import Estudiante
from personero.serializers.candidatoSerializer import CandidatoSerializer
from personero.serializers.estudianteSerializer import EstudianteSerializer
from personero.modelos.voto import Voto
from rest_framework import serializers

class VotoSerializer(serializers.ModelSerializer):
    estudiante = serializers.IntegerField()
    candidato = serializers.IntegerField()

    class Meta:
        model = Voto
        fields = ['fecha', 'hora', 'estudiante', 'candidato']

    def create(self, validated_data):
        estudianteData = validated_data.pop('estudiante')
        estudiante = Estudiante.objects.get(id = estudianteData)

        candidatoData = validated_data.pop('candidato')
        candidato = Candidato.objects.get(id= candidatoData)

        voto = Voto.objects.create(candidato = candidato, estudiante = estudiante, **validated_data)
        return voto
    
    def to_representation(self, obj):
        estudiante = Estudiante.objects.get(id = obj.estudiante.id)
        candidato = Candidato.objects.get(id = obj.candidato.id)
        return {
            'fecha': obj.fecha,
            'hora': obj.hora,
            'estudiante': EstudianteSerializer(estudiante).data,
            'candidato': CandidatoSerializer(candidato).data
        }