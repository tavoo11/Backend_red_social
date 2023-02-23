from django.db import models
from .foto import Foto
from .usuario import Usuario

class Likes (models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='likes_usuario')
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name='likes_fotos')

    class Meta:
        unique_together = ('usuario', 'foto')