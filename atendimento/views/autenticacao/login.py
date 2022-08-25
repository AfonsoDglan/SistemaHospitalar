from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from atendimento.forms.formLogin import LoginForm



class LoginView(View):
    
    def get(self, request):
        template_name = 'autenticacao/login.html'
        context = {}
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        
        context['form'] = LoginForm()
        return render(request,template_name,context)
    
    def post(self, request):
        template_name = 'autenticacao/login.html'
        context = {}
        form = LoginForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        
        context['form'] = form
        context['error'] = "Usuário ou senha inválidos"
        return render(request, template_name, context)

