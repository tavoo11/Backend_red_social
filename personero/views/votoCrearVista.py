from rest_framework import generics
from personero.serializers.votoSerializer import VotoSerializer
from personero.modelos.voto import Voto
from rest_framework.response import Response
from rest_framework import  status

class VotoList(generics.ListCreateAPIView):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer

    def post(self, request, *args, **kwargs):
        serializer = VotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

