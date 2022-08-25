import os, datetime
from datetime import datetime, date
from django.template.defaultfilters import slugify
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
import calendar


def retornaMesExtenso(value):
    mes_ext = {1: 'Janeiro', 2 : 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6 : 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12:'Dezembro'}

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
def retira_acento_upload(objeto, arquivo):
  
    caminho = str( '%s/%s/%s' % ( objeto._meta.app_label, objeto.__class__.__name__, datetime.now().year )).lower()
    nome, ext = os.path.splitext( arquivo )

    url = slugify( nome[:30] )

    return os.path.join( 'uploads', caminho, url+ext )


def caminho_upload(objeto, arquivo):
    caminho = str('%s/%s/%s' % (objeto._meta.app_label, objeto.__class__.__name__, objeto.semestre)).lower()
    nome, ext = os.path.splitext(arquivo)

    url = slugify(nome[:30])

    return os.path.join('uploads', caminho, url + ext)

def subtrairDiasData(data, dias):

    hoje = data
    intervalo = timedelta(dias)
    newdata =  hoje - intervalo
    
    return newdata


def somarDiasData(data, dias):

    hoje = data
    intervalo = timedelta(dias)
    newdata =  hoje + intervalo
    
    return newdata

def somarMesesData(data, meses):

    hoje = data    
    newdata =  hoje + relativedelta(months=meses)
    #parametros['inicio']+timedelta(days=6)
    
    return newdata

def subtrairMesesData(data, meses):

    hoje = data    
    newdata =  hoje - relativedelta(months=meses)
    #parametros['inicio']+timedelta(days=6)
    
    return newdata

def subtrairHorasDataHora(data, horas):

    hoje = data    
    newdata =  hoje - relativedelta(hours=horas)
    #parametros['inicio']+timedelta(days=6)
    
    return newdata

def subtrairMinutosDataHora(hora, minutos):

    # hoje = data    
    dataAtual = datetime.now().date()
    data1 = str(dataAtual) + " " + str(hora)
    # data2 = str(dataAtual) + " " + str(horaFinal)

    d1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
    newdata =  d1 - relativedelta(minutes=minutos)
    #parametros['inicio']+timedelta(days=6)
    
    return newdata.time()

def somarMinutosDataHora(hora, minutos):

    # hoje = data    
    dataAtual = datetime.now().date()
    data1 = str(dataAtual) + " " + str(hora)
    # data2 = str(dataAtual) + " " + str(horaFinal)

    d1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
    newdata =  d1 + relativedelta(minutes=minutos)
    #parametros['inicio']+timedelta(days=6)
    
    return newdata.time()

def daterange(start_date, end_date):
    if start_date:
        # WTR - 08/12/2016 INCLUI O +1, POIS Ñ TVA ADD O ULTIMO DIA DO RANGE
        for n in range(int ((end_date - start_date).days+1)):
            yield start_date + timedelta(n)

def retornaFistLastDayMes(ano, mes):
    diaMes={}
    
    diaMesFistLast = calendar.monthrange(ano, mes) 
    diaMes['inicial'] = datetime.strptime('01'+str(mes)+str(ano), '%d%m%Y').date()
    diaMes['final'] = datetime.strptime(str(diaMesFistLast[1])+str(mes)+str(ano), '%d%m%Y').date()

    return diaMes

# RETORNA O DIA DA SEMANA DO PYTHON
# 0 (represendo segunda-feira) e 6 (representando domingo).
# NO SIE OS DIAS SÃO DIFERENTES
def retornaDiaSemanaPython(diaSIE):

    if diaSIE==1 or diaSIE==8:
        return 6

    if diaSIE==2: #segunda
        return 0
    if diaSIE==3: #terca
        return 1
    if diaSIE==4: #quarta
        return 2
    if diaSIE==5: #quinta
        return 3
    if diaSIE==6: #sexta
        return 4
    if diaSIE==7: #sabado
        return 5

# # ENTRADA: DIA SEMANA SIE
# # SAÍDA: DIA SEMANA PYTHON
# def retornaDiaSemanaSIE(do):

#     if self.turma.diaSemana==2:
#         return 0#segunda
#     if self.turma.diaSemana==3:
#         return 1#terça
#     if self.turma.diaSemana==4:
#         return 2#quarta
#     if self.turma.diaSemana==5:
#         return 3#quinta
#     if self.turma.diaSemana==6:
#         return 4#sexta
#     if self.turma.diaSemana==7:
#         return 5#sabado

#     return 0#indefinido

def retornaInicioSemana(day):
    day_of_week = day.weekday()

    to_beginning_of_week = timedelta(days=day_of_week)
    beginning_of_week = day - to_beginning_of_week



    to_end_of_week = timedelta(days=6 - day_of_week)
    end_of_week = day + to_end_of_week

    #raise Exception(end_of_week)#hj 2 beginning_of_week=23 end_of_week=

    return (beginning_of_week, end_of_week)

def int_to_roman(input): 
    if not isinstance(input, type(1)): 
        #raise TypeError, "expected integer, got %s" % type(input) 
        pass

    if not 0 < input < 4000: 
        #raise ValueError, "Argument must be between 1 and 3999" 
        pass

    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1) 
    nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I') 
    result = [] 

    for i in range(len(ints)): 
        count = int(input / ints[i]) 
        result.append(nums[i] * count) 
        input -= ints[i] * count 

    return ''.join(result)

# CONTA A DIFERENCA ENTRE DUAS DATAS + 1
# EXEMPLO: 
#       DATA 1: 10/02/2016 
#       DATA 2: 20/02/2016
#       resultado: 11 DIAS, OU SEJA ENTRE DIA 10 E 20...FORAM 11 DIAS
def diffDate(data1, data2): 
    d1 = data1 
    d2 = data2 

    delta = d2-d1 
    r = delta.days+1 if (delta.days > 0) else "erro"

    return r

    #return (beginning_of_week, end_of_week)

def diffTimeIntervalo(horaInicial, horaFinal, intervalo): 

    dataAtual = datetime.now().date()
    data1 = str(dataAtual) + " " + str(horaInicial)
    data2 = str(dataAtual) + " " + str(horaFinal)

    d1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
    d2 = datetime.strptime(data2, "%Y-%m-%d %H:%M:%S")
    d2 = d2 - timedelta(minutes=intervalo)
    result = d2 - d1

    return abs(result)

def convertSegundosHora(qtdSegundos):
    dias = qtdSegundos // 86400
    segundos_rest = qtdSegundos % 86400
    horas = segundos_rest // 3600
    segundos_rest = segundos_rest % 3600
    minutos = segundos_rest // 60
    segundos_rest = segundos_rest % 60
    
    horas=horas+(dias*24)
    txtRetorno = str(horas)+' horas '+str(minutos)+' minutos'        

    dictRetorno={}
    dictRetorno['descricao'] = txtRetorno
    dictRetorno['dias'] = dias
    dictRetorno['horas'] = horas
    dictRetorno['minutos'] = minutos    
    dictRetorno['segundos'] = segundos_rest
        
    return dictRetorno
    #converter dias em HORAS    
    # print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")


def retornaDiaDaSemana(dia):
  dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')

  return dias[dia]

def retornaNomeAbreviado(pessoa):
	#raise Exception(pessoa.id)
	arrayNome = pessoa.split(' ')
	return arrayNome[0] + ' ' + arrayNome[-1]


def retornaAbreviacaoFrase(frase):

	novoNome=''
	espaco = " "
	fraseArray = frase.split()
	for i, palavra in enumerate(fraseArray):

		if i==len(fraseArray)-1:
			espaco = ""

		novoNome += verificaPalavraArray(palavra)+espaco


	return novoNome

def verificaPalavraArray(palavra):

  meuArray={}
  arrayPalavras=[]

  '''
  arrayPalavras.append({'0': 'da', '1': ''})
  arrayPalavras.append({'0': 'do', '1': ''})
  arrayPalavras.append({'0': 'de', '1': ''})
  '''
  arrayPalavras.append({'0': 'e', '1': ''})


  arrayPalavras.append({'0': 'A', '1': ''}) 
  arrayPalavras.append({'0': 'Administração', '1': 'Administ.'}) 	
  arrayPalavras.append({'0': 'Apresentação', '1': 'Apresent.'})
  arrayPalavras.append({'0': 'Arquitetura', '1': 'Arquit.'})
  arrayPalavras.append({'0': 'Assistência', '1': 'Assistên.'})
  arrayPalavras.append({'0': 'Adolescente', '1': 'Adolesc.'})
  arrayPalavras.append({'0': 'Aprendizagem', '1': 'Aprendiz.'})
  arrayPalavras.append({'0': 'Aplicabilidade', '1': 'Aplicabil.'})
  arrayPalavras.append({'0': 'Avançadas', '1': 'Avanç.'})
  arrayPalavras.append({'0': 'Adoecimento', '1': 'Adoecim.'})
  arrayPalavras.append({'0': 'Aplicações', '1': 'Aplicaç.'})
  
  

  arrayPalavras.append({'0': 'Coordenação', '1': 'Coord.'})
  arrayPalavras.append({'0': 'Comunitária', '1': 'Comunit.'})	
  arrayPalavras.append({'0': 'Contemporânea', '1': 'Contempor.'})
  arrayPalavras.append({'0': 'Construções', '1': 'Constru.'})
  arrayPalavras.append({'0': 'Conservação', '1': 'Conserv.'})
  arrayPalavras.append({'0': 'Cirúrgico', '1': 'Cirúrg.'})
  arrayPalavras.append({'0': 'Cuidados', '1': 'Cuidad.'})
    
  arrayPalavras.append({'0': 'Desenvolvimento', '1': 'Desenvolv.'})
  arrayPalavras.append({'0': 'Diferenciais', '1': 'Diferenc.'})
  arrayPalavras.append({'0': 'Diversidade', '1': 'Diversid.'})

  arrayPalavras.append({'0': 'Elaboração', '1': 'Elaboraç.'})
  arrayPalavras.append({'0': 'Estatística', '1': 'Estatíst.'})
  arrayPalavras.append({'0': 'Equipamentos', '1': 'Equipam.'})
  arrayPalavras.append({'0': 'Energéticos', '1': 'Energét.'})
  arrayPalavras.append({'0': 'Engenharia', '1': 'Engenh.'})
  arrayPalavras.append({'0': 'Em', '1': ''})

  arrayPalavras.append({'0': 'Fundamentos', '1': 'Fundam.'})
  arrayPalavras.append({'0': 'Gerenciamento', '1': 'Gerenc.'})

  arrayPalavras.append({'0': 'Hidráulicos', '1': 'Hidrául.'})

  arrayPalavras.append({'0': 'Integralidade', '1': 'Integralid.'})
  arrayPalavras.append({'0': 'Informações', '1': 'Informa.'})
  arrayPalavras.append({'0': 'Industriais', '1': 'Indust.'})	
  arrayPalavras.append({'0': 'Informação', '1': 'Informa.'})
  arrayPalavras.append({'0': 'Interdisciplinares', '1': 'Interdisc.'})
  arrayPalavras.append({'0': 'Instalações', '1': 'Instalaç.'})
  arrayPalavras.append({'0': 'Intervenção', '1': 'Interv.'})
  arrayPalavras.append({'0': 'Instrumental', '1': 'Instrument.'})
  arrayPalavras.append({'0': 'Institucionais', '1': 'Instituc.'})
    
  arrayPalavras.append({'0': 'Laboratório', '1': 'Laborat.'})
  arrayPalavras.append({'0': 'Macroeconômica', '1': 'Macroecon.'})
  arrayPalavras.append({'0': 'Modelagem', '1': 'Model.'})
    

  arrayPalavras.append({'0': 'Patrimoniais', '1': 'Patrimon.'})
  arrayPalavras.append({'0': 'Planejamento', '1': 'Planej.'})
  arrayPalavras.append({'0': 'Patológicos', '1': 'Patológic.'})
  arrayPalavras.append({'0': 'populacionais', '1': 'populac.'})
  arrayPalavras.append({'0': 'populacionais-', '1': 'populac.'})
  arrayPalavras.append({'0': 'Populacionais', '1': 'Populac.'})
    
  arrayPalavras.append({'0': 'Organizacional', '1': 'Organizac.'})
  arrayPalavras.append({'0': 'Organização', '1': 'Organizac.'})

  arrayPalavras.append({'0': 'Orçamentária', '1': 'Orçamentar.'})
  arrayPalavras.append({'0': 'Patológicos', '1': 'Patológ.'})
  arrayPalavras.append({'0': 'Patológicos:', '1': 'Patológ.'})
  arrayPalavras.append({'0': 'Probabilidade', '1': 'Probabil.'})
    
  arrayPalavras.append({'0': 'Relacionamento', '1': 'Relacionam.'})
  arrayPalavras.append({'0': 'Reprodutivo', '1': 'Reprod.'})
  arrayPalavras.append({'0': 'Recuperação', '1': 'Recuper.'})


  arrayPalavras.append({'0': 'Sanitários', '1': 'Sanitár.'})
  arrayPalavras.append({'0': 'Supervisionado', '1': 'Supervis.'})


  arrayPalavras.append({'0': 'Tecnologia', '1': 'Tecnolog.'})
  arrayPalavras.append({'0': 'Transmissíveis', '1': 'Transmissiv.'})
      
  for chekPalavra in arrayPalavras:


    if chekPalavra['0']==palavra:
      return chekPalavra['1']


  return palavra
