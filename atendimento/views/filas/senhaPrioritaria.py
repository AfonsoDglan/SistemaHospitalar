from django.views.generic import TemplateView
from atendimento.models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class SenhaPrioritaria(TemplateView):
    model = Senha
    def get(self, request):
        ultimaSenha = Senha.objects.filter(tipo=2).count()
        senha = 'P - ' + str(ultimaSenha+1)
        request.session['senha'] = senha
        senhaBanco = Senha.objects.create(senha=senha,status=1,tipo=2)
        return HttpResponseRedirect(reverse_lazy('atendimento:minhaSenha')) 
    