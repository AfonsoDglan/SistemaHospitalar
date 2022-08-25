from dataclasses import field
from django.forms import *
from atendimento.models import *
class TriagemForm(ModelForm):
    class Meta:
        model = Triagem
        fields = "__all__"
        exclude = ["atendente","estado"]
        
        widgets = {
            "nomePaciente": TextInput(attrs={'class': 'enfinput','placeholder':'Nome do Paciente','required': True}),
            "queixaPrincipal": Textarea(attrs={'class': 'enfinput','placeholder':'Queixas Apresentadas Pelo Paciente','required': True}),
            "historicoBreve": Textarea(attrs={'class': 'enfinput','placeholder':'Historico Do Paciente','required': True}),
            "observacaoObjetiva": Textarea(attrs={'class': 'enfinput','placeholder':'Observações a Serem Concideradas.'}),
            "frequenciaCardiaca": NumberInput(attrs={'class': 'enfinput','required': True,'placeholder':'Qual a freqência cardíaca do paciênte?'}),
            "frequenciaRespiratoria": NumberInput(attrs={'class': 'enfinput','required': True,'placeholder':'Qual a freqência respiratória do paciênte?'}),
            "sexo": Select(attrs={'class': 'enfinput','required': True}),
            "dor": Select(attrs={'class': 'enfinput','required': True}),
            "pressaoArterial": NumberInput(attrs={'class': 'enfinput','required': True,'placeholder':'Qual a pressão arterial do paciênte?'}),
            "temperatura": NumberInput(attrs={'class': 'enfinput','required': True,'placeholder':'Qual a temperatura do paciênte?'}),
            "classificacao": Select(attrs={'class': 'enfinput','required': True}),
        }
            