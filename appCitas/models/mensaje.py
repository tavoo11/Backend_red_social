from django.db import models
from .usuario import Usuario

class Mensaje(models.Model):
    id = models.BigAutoField(primary_key=True)
    contenido = models.CharField(max_length=255)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    id_emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes_enviados')
    id_receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensajes_recibidos')