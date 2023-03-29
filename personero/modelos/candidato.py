from django.db import models

class Candidato(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    propuesta = models.TextField()
    imagen = models.TextField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido