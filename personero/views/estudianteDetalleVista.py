from rest_framework import generics
from personero.serializers.estudianteSerializer import EstudianteSerializer
from personero.modelos.estudiante import Estudiante
from rest_framework.response import Response
from rest_framework import  status

class EstudianteDetalleVista(generics.CreateAPIView):
    serializer_class = EstudianteSerializer
    queryset = Estudiante.objects.all()

    def get(self, request, *args, **kwargs):
        estudiante = self.get_object()
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        estudiante = self.get_object()
        serializer = EstudianteSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        estudiante = self.get_object()
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
