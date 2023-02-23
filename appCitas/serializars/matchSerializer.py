from appCitas.models.match import Match
from appCitas.models.usuario import Usuario
from .usuarioSerializer import UsuarioSerializer
from rest_framework import serializers

class MatchSerializer(serializers.ModelSerializer):
    id_usuario1 = serializers.IntegerField()
    id_usuario2 = serializers.IntegerField()
    class Meta:
        model = Match
        fields = ['id', 'fecha_hora', 'id_usuario1', 'id_usuario2']

    def create(self, validated_data):
        usuario1Data = validated_data.pop('id_usuario1')
        usuario2Data = validated_data.pop('id_usuario2')

        usuario1 = Usuario.objects.get(id=usuario1Data)
        usuario2 = Usuario.objects.get(id=usuario2Data)

        match = Match.objects.create(id_usuario1=usuario1, id_usuario2=usuario2, **validated_data)
        return match

    
    def to_representation(self, obj):
       usuario1 = Usuario.objects.get(id=obj.id_usuario1.id)
       usuario2 = Usuario.objects.get(id=obj.id_usuario2.id)
       return {
        'id': obj.id,
        'fecha_hora': obj.fecha_hora,
        'id_usuario1': UsuarioSerializer(usuario1).data,
        'id_usuario2': UsuarioSerializer(usuario2).data,
       }