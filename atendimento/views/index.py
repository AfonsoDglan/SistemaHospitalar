from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    
    def get(self, request):
        template_name = 'index.html'
        context = {}
        context['user'] = request.user
        return render(request, template_name, context)