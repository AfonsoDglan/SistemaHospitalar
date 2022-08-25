from django.views.generic import View
from atendimento.models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class SenhaConvencional(View):
    model = Senha
    def get(self, request):
        ultimaSenha = Senha.objects.filter(tipo=1).count()
        senha = 'C - ' + str(ultimaSenha+1)
        request.session['senha'] = senha
        senhaBanco = Senha.objects.create(senha=senha,status=1,tipo=1)
        return HttpResponseRedirect(reverse_lazy('atendimento:minhaSenha'))
    
    