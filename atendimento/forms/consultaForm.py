from dataclasses import field
from django.forms import *
from atendimento.models import *
class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ["diagnostico"]
        widgets = {"diagnostico": Textarea(attrs={'class': 'medtextbox','placeholder':'Diagnostico','required': True})}
        