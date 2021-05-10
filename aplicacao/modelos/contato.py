from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    mensagem = models.TextField()