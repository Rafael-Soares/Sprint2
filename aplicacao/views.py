from django.shortcuts import render
#from .models import *
#importação do contato
from .forms import ServicoForms, ContatoForms
from django.core.mail import send_mail

def index(request):
     # INICIALIZANDO AS VARIVÁVEIS GLOBAIS DA FUNÇÃO DE FORMA VAZIA
    form_servico = ''
    form_contato = ''
    # VERIFICAÇÃO PARA ENVIO DE EMAIL
    if request.method == 'POST':
        form_servico = ServicoForms(request.POST)
        if form_servico.is_valid():  # SE O FORMULÁRIO DE PROPOSTA DOS SERVIÇOS FOR VÁLIDO
            form_servico.send_mail()
            form_servico = ServicoForms()
            form_contato = ContatoForms()
        else:                        # SE NÃO FOR, VAI VERIFICAR SE O FORM DE CONTATO É VÁLIDO
            form_contato = ContatoForms(request.POST)
            if form_contato.is_valid():
                form_contato.send_mail()
                form_contato = ContatoForms()
                form_servico = ServicoForms()
    else:                              # SE NENHUM DOS DOIS FOR VÁLIDO
        form_contato = ContatoForms()
        form_servico = ServicoForms()
    context = {
        'form_servico': form_servico,
        'form_contato': form_contato
    }
    return render(request, 'index.html', context)