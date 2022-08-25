import re
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404, HttpResponse
from atendimento.forms.triagemForm import *
from atendimento.models import *
from django.shortcuts import render
from django.urls import reverse_lazy
from atendimento.views import *

from atendimento.models import senhas

class TriagemView(LoginRequiredMixin,TemplateView):
    def dispatch(self, request):
        pessoa = Pessoa.objects.get(user = request.user)
        if(pessoa.tipo == 2):
            return super().dispatch(request)
        else:
            return HttpResponseRedirect(reverse_lazy('index'))
        
    
    def get(self,request):
        template_name = 'base/triagem.html'
        if Senha.objects.filter(status=1).count() == 0:
            raise "Não temos mais senhas para atender no momento."
        else:
            if Senha.objects.filter(tipo=2,status=1).count() != 0:
                senha = Senha.objects.filter(tipo=2,status=1)[0]
            else:
                senha = Senha.objects.filter(tipo=1,status=1)[0]
        form = TriagemForm()
        form.fields['senha'].widget.attrs={'class': 'enfinput','value':senha}
        context = {'form': form}
        return render(request, template_name,context)
    
    def post(self, request):
        template_name = 'base/triagem.html'
        context = {}
        form = TriagemForm(request.POST)
        if form.is_valid():
            atendente = Pessoa.objects.get(user=request.user)
            obj = form.save(commit=False)
            obj.atendente = atendente
            obj.estado = 1
            obj.save()
            Senha.objects.filter(senha=request.POST.get('senha')).update(status=2)
            return render(request, template_name,context)
        else:
            return HttpResponse("não valido")
    
    
