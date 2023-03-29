from django.db import models
from personero.modelos.candidato import Candidato
from personero.modelos.estudiante import Estudiante

class Voto(models.Model):
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE) 