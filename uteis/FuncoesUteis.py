import os, datetime
from datetime import datetime
from django.utils.text import format_lazy
from django.template.defaultfilters import slugify

class FuncoesUteis():

    def retornaMesExtenso(value):
        mes_ext = {1: 'Janeiro', 2 : 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6 : 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12:'Dezembro'}

        return mes_ext[int(value)]

    @staticmethod
    def retornaDiaSemanaExtenso(value):
        mes_ext = {0: 'Segunda-feira', 1 : 'Terça-feira', 2: 'Quarta-feira', 3: 'Quinta-feira', 4: 'Sexta-feira', 5 : 'Sábado', 6: 'Domingo'}

        return mes_ext[int(value)]

    '''
        Essa função irá normalizar como um slug, o nome do arquivo que está sendo gravado e, irá gravá-lo
        em /media/uploads/APPNAME_CLASSNAME/ANO/nome_do_arquivo_normalizado.extensao
        customize o return da def acima da maneira que desejar. 
        No exemplo acima, o arquivo será enviado para:
        uploads/<nome_da_app>/<nome_da_classe>/<ano_atual>/<nome_do_arquivo_nomalizado>.<extensão>
        Models
            arquivo = models.FileField(upload_to=retira_acento_upload)
    '''  
    @staticmethod
    def retira_acento_upload(objeto, arquivo):
    
        caminho = str( '%s/%s/%s' % ( objeto._meta.app_label, objeto.__class__.__name__, datetime.now().year )).lower()
        nome, ext = os.path.splitext( arquivo )

        url = slugify( nome[:30] )

        return os.path.join( 'uploads', caminho, url+ext )


def retira_acento_upload(objeto, arquivo):

    caminho = str( '%s/%s/%s' % ( objeto._meta.app_label, objeto.__class__.__name__, datetime.now().year )).lower()
    nome, ext = os.path.splitext( arquivo )

    url = slugify( nome[:30] )

    return os.path.join( 'uploads', caminho, url+ext )