from models.usuario import Usuario
from models.foto import Foto
from .usuarioSerializer import UsuarioSerializer
from rest_framework import serializers

class FotoSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField()

    class Meta:
        model = Foto
        fields = '__all__'

    def create(self, validated_data):
        usuarioData = validated_data.pop('id_usuario')
        usuario = Usuario.objects.get(id = usuarioData)

        foto = Foto.objects.create(id_usuario = usuario, **validated_data)
        return foto

    def to_representation(self, obj):
        usuario = Usuario.objects.get(id=obj.id_usuario1.id)
        return {
            'id': obj.id,
            'imagen_base64': obj.imagen_base64,
            'descripcion': obj.descripcion,
            'fecha_hora': obj.fecha_hora,
            'usuario': UsuarioSerializer(usuario).data
        }

