from django import forms
from django.core.mail import send_mail
from django.conf import settings
from .mail import send_mail_template
from aplicacao.classe_servico import tipos_de_servico
from .modelos.classe_servico import Classe_Servico
from .modelos.servico import Servico
from .modelos.contato import Contato

class ServicoForms(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        labels = {'classe_servico':'Tipos de serviço', 'telefone':'Telefone', 'email':'E-mail', 'nome': 'Nome'}

    def clean(self):
        servico_cliente = self.cleaned_data.get('classe_servico')
        tel = self.cleaned_data.get('telefone')
        email_cliente = self.cleaned_data.get('email')
        name = self.cleaned_data.get('nome')
        #falta fazer as validações
        return self.cleaned_data
    def send_mail(self):
        assunto = 'Solicitação de serviço'
        context = {
            'servicos': self.cleaned_data.get('classe_servico'),
            'telefone': self.cleaned_data.get('telefone'),
            'nome':     self.cleaned_data.get('nome'),
            'email':    self.cleaned_data.get('email'),
        }

        template_html = 'solicite.html'
        send_mail_template(assunto, template_html, context, [settings.CONTACT_EMAIL])

class ContatoForms(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        labels = {'nome':'Nome', 'telefone':'Telefone', 'email':'E-mail', 'mensagem':'Mensagem'}




    def send_mail(self):
        assunto = 'Dúvida'
        context = {
            'nome':     self.cleaned_data.get('nome'),
            'telefone': self.cleaned_data.get('telefone'),
            'email':    self.cleaned_data.get('email'),
            'mensagem': self.cleaned_data.get('mensagem')
        }

        template_html = 'contato.html'
        send_mail_template(assunto, template_html, context, [settings.CONTACT_EMAIL])

