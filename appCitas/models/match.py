from django.db import models
from .usuario import Usuario

class Match(models.Model):
    id = models.BigAutoField(primary_key=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    id_usuario1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='matchs1')
    id_usuario2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='matchs2')