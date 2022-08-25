from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpRequest, Http404
from atendimento.forms.consultaForm import ConsultaForm
from atendimento.forms.triagemForm import *
from atendimento.models import *
from django.shortcuts import render
from django.urls import reverse_lazy

from atendimento.models.Triagem import Triagem

class ConsultaView(LoginRequiredMixin,TemplateView):
    def dispatch(self, request):
        pessoa = Pessoa.objects.get(user = request.user)
        if(pessoa.tipo == 1):
            return super().dispatch(request)
        else:
            return HttpResponseRedirect(reverse_lazy('index'))

    def get(self,request):
        template_name = 'base/consulta.html'
        form = ConsultaForm()
        if Triagem.objects.filter(classificacao=1,estado=1).count() != 0:
            triagem = Triagem.objects.filter(classificacao=1,estado=1)[0]
        elif Triagem.objects.filter(classificacao=2,estado=1).count() != 0:
            triagem = Triagem.objects.filter(classificacao=2,estado=1)[0]
        elif Triagem.objects.filter(classificacao=3,estado=1).count() != 0:
            triagem = Triagem.objects.filter(classificacao=3,estado=1)[0]
        elif Triagem.objects.filter(classificacao=4,estado=1).count() != 0:
            triagem = Triagem.objects.filter(classificacao=1,estado=1)[0]
        elif Triagem.objects.filter(classificacao=5,estado=1).count() != 0:
            triagem = Triagem.objects.filter(classificacao=1,estado=1)[0]
        else:
            raise "No Momento Não Temos Paciente Na Triagem Para Ser Atendido"
        context = {'form': form,
                   'nomePaciente':triagem.nomePaciente,
                   'queixa': triagem.queixaPrincipal,
                   'historico': triagem.historicoBreve,
                   'obs': triagem.observacaoObjetiva,
                   'dor': triagem.dor,
                   'fc': triagem.frequenciaCardiaca,
                   'fr': triagem.frequenciaRespiratoria,
                   'pa': triagem.pressaoArterial,
                   'temp': triagem.temperatura}
        return render(request, template_name,context)
    
    def post(self, request):
        template_name = 'base/triagem.html'
        context = {}
        form = ConsultaForm(request.POST)
        if form.is_valid():
            if Triagem.objects.filter(classificacao=1,estado=1).count() != 0:
                triagem = Triagem.objects.filter(classificacao=1,estado=1)[0]
            elif Triagem.objects.filter(classificacao=2,estado=1).count() != 0:
                triagem = Triagem.objects.filter(classificacao=2,estado=1)[0]
            elif Triagem.objects.filter(classificacao=3,estado=1).count() != 0:
                triagem = Triagem.objects.filter(classificacao=3,estado=1)[0]
            elif Triagem.objects.filter(classificacao=4,estado=1).count() != 0:
                triagem = Triagem.objects.filter(classificacao=1,estado=1)[0]
            elif Triagem.objects.filter(classificacao=5,estado=1).count() != 0:
                triagem = Triagem.objects.filter(classificacao=1,estado=1)[0]
            else:
                raise "Não temos mais pacientes na triagem"
            triagem = Triagem.objects.get(id=triagem.id)
            obj = form.save(commit=False)
            obj.paciente = triagem
            obj.medicoAtendente = Pessoa.objects.get(user=request.user)
            obj.save()
            Triagem.objects.filter(id=triagem.id).update(estado=2)
            return render(request, template_name,context)
        else:
            return Http404()
        