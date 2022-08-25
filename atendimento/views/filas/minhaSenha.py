from django.views.generic import TemplateView
from django.shortcuts import render

class MinhaSenhaView(TemplateView):
    template_name = 'senhas/senhas.html'