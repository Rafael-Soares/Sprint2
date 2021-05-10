from django.db import models
from django.utils.translation import gettext_lazy as _

class Classe_Servico(models.TextChoices):
        SERVICO_1 = 'SER1', _('Serviço 1')
        SERVICO_2  = 'SER2', _('Serviço 2')
        SERVICO_3  = 'SER3', _('Serviço 3')
        SERVICO_4  = 'SER4', _('Serviço 4')
        SERVICO_5  = 'SER5', _('Serviço 5')
        