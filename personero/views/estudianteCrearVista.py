from rest_framework import generics
from personero.serializers.estudianteSerializer import EstudianteSerializer
from personero.modelos.estudiante import Estudiante

class EstudianteCrearVista(generics.CreateAPIView):
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()
