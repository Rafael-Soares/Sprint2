from django.db import models
from datetime import datetime

class QuemSomo(models.Model):
    descricao = models.TextField('Descrição', blank=True)

class Missao(models.Model):
    descricao = models.TextField('Descrição', blank=True)

class Visao(models.Model):
    descricao = models.TextField('Descrição', blank=True)

class Valores(models.Model):
    descricao = models.TextField('Descrição', blank=True)

class Servicos(models.Model):
    title_servico = models.CharField('Título do Serviço', max_length=50)
    imagem_servico = models.ImageField('Imagem do serviço', upload_to='imagens/', blank=True)
    descricao_servico = models.TextField('Descrição do serviço', blank=True)

class Portifolio(models.Model):
    title_portfolio = models.CharField('Título', max_length=50)
    descricao_portfolio = models.TextField('Descrição')