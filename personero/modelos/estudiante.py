from django.db import models

class Estudiante(models.Model):
    cedula = models.CharField(max_length=20)

    def __str__(self):
        return self.cedula