from django.contrib import admin

# Register your models here.
from atendimento.models import *

class PessoaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Pessoa, PessoaAdmin)
