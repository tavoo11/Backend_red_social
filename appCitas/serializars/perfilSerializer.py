from appCitas.models.perfil import Perfil
from rest_framework import serializers

class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil 
        fields = ['id','descripcion', 'imagen']
