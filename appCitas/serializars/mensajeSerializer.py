from rest_framework import serializers
from appCitas.models import Mensaje
from appCitas.models.usuario import Usuario
from .usuarioSerializer import UsuarioSerializer

class MensajeSerializer(serializers.ModelSerializer):
    id_emisor = serializers.IntegerField()
    id_receptor = serializers.IntegerField()
    
    class Meta:
        model = Mensaje
        fields = ['id', 'contenido', 'fecha_hora', 'id_emisor', 'id_receptor']

    
    def create(self, validated_data):
        emisor_id = validated_data.pop('id_emisor')
        receptor_id = validated_data.pop('id_receptor')

        emisor = Usuario.objects.get(id=emisor_id)
        receptor = Usuario.objects.get(id=receptor_id)


        mensaje = Mensaje.objects.create(id_emisor=emisor, id_receptor=receptor, **validated_data)
        return mensaje
    
    def to_representation(self, obj):
        emisor = Usuario.objects.get(id=obj.id_emisor.id)
        receptor = Usuario.objects.get(id=obj.id_receptor.id)
        return {
            'id': obj.id,
            'contenido': obj.contenido,
            'fecha_hora': obj.fecha_hora,
            'id_emisor': UsuarioSerializer(emisor).data,
            'id_receptor': UsuarioSerializer(receptor).data,
        }



