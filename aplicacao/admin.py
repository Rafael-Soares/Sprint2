from django.contrib import admin
from .models import *

class Listando(admin.ModelAdmin):
    list_display = ('id', 'descricao')
    list_display_links = ('id', 'descricao')
    list_per_page = 3
admin.site.register(QuemSomo, Listando)
admin.site.register(Missao, Listando)
admin.site.register(Visao, Listando)
admin.site.register(Valores, Listando)

class ListandoServicos(admin.ModelAdmin):
    list_display = ('id', 'title_servico', 'descricao_servico')
    list_display_links = ('id', 'title_servico')
    list_per_page = 3

admin.site.register(Servicos, ListandoServicos)

class ListandoPortfolio(admin.ModelAdmin):
    list_display = ('id', 'title_portfolio', 'descricao_portfolio')
    list_display_links = ('id', 'title_portfolio')
    list_per_page = 3
admin.site.register(Portifolio, ListandoPortfolio)