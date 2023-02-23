from django.db import models


class Perfil(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    imagen = models.TextField()