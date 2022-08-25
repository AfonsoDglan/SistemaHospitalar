from django.views.generic import TemplateView
from django.shortcuts import render
class PedirSenhaView(TemplateView):
    template_name = 'senhas/pedirSenha.html'