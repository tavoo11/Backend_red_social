from django.db import models
from .usuario import Usuario

class Foto (models.Model):
    id = models.BigAutoField(primary_key=True)
    imagen_base64 = models.TextField()
    descripcion = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Usuario, related_name='fotos_like')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='fotos')

    class Meta:
        db_table = 'fotos'