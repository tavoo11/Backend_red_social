from rest_framework import serializers
from appCitas.models.usuario import Usuario
from appCitas.serializars.perfilSerializer import PerfilSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()
    class Meta:
        model = Usuario
        fields = ['id','username', 'password', 'nombre', 'apellidos', 'email', 'fechaNacimiento', 'genero', 'intereses', 'perfil']


    def create(self, validated_data):
        perfil_data = validated_data.pop('perfil')
        perfil = PerfilSerializer().create(perfil_data)
        usuario_instancia = Usuario.objects.create(perfil = perfil, **validated_data)
        return usuario_instancia

    def to_representation(self, obj):
        return {
            'id': obj.id,
            'username': obj.username, 
            'password': obj.password, 
            'nombre': obj.nombre, 
            'apellidos': obj.apellidos, 
            'email': obj.email, 
            'fechaNacimiento': obj.fechaNacimiento, 
            'genero': obj.genero, 
            'intereses': obj.intereses, 
            'perfil': PerfilSerializer(obj.perfil).data
        }