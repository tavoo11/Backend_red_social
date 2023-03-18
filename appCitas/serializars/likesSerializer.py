from ..models.foto import Foto
from ..models.likes import Likes
from ..models.usuario import Usuario
from  ..serializars.usuarioSerializer import UsuarioSerializer
from ..serializars.fotoSerializer import FotoSerializer
from rest_framework import serializers

class LikeSerializer(serializers.ModelSerializer):
    usuario = serializers.IntegerField()
    foto = serializers.IntegerField()

    class Meta:
        model = Likes
        fields = ['id', 'id_usuario', 'id_foto']

    def create(self, validated_data):
        usuarioData = validated_data.pop('id_usuario')
        usuario = Usuario.objects.get(id = usuarioData)
        fotoData = validated_data.pop('id_foto')
        foto = Foto.objects.get(id = fotoData)

        like = Likes.objects.create(id_usuario = usuario, id_foto = foto, **validated_data)
        return like

    def to_representation(self, obj):
        usuario = Usuario.objects.get(id = obj.id_usuario.id)
        foto = Foto.objects.get(id = obj.id_foto.id)
        return {
            'id': obj.id,
            'id_usuario': UsuarioSerializer(usuario).data,
            'id_foto': FotoSerializer(foto).data
        }