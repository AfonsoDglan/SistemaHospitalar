from django.db import models
from atendimento.models import *

class Consulta(models.Model):
    paciente = models.ForeignKey(Triagem, editable=False, on_delete=models.PROTECT)
    medicoAtendente = models.ForeignKey(Pessoa, editable=False, on_delete=models.PROTECT)
    diagnostico = models.TextField('Diagnostico médico', blank=True, null=True)