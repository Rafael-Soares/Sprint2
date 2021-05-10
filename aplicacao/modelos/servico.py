from django.db import models
from .classe_servico import Classe_Servico

class Servico(models.Model):
    classe_servico = models.CharField(max_length=5,choices=Classe_Servico.choices, default=0)
    telefone = models.CharField( max_length=12)
    email = models.CharField(max_length=20)
    nome = models.CharField(max_length=50)
    