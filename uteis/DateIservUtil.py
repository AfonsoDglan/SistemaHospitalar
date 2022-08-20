from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

class DateIservUtil():

    
    '''
    parametro:
        days (dias)
        seconds (segundos)
        microseconds (microsegundos)
        milliseconds (milisegundos)
        minutes (minutos)
        hours (horas)
        weeks (semanas)
    '''
    @staticmethod
    def somarHorasDatetime(data, quantidade):

        # data1 = str(data) + " " + str(hora)
        # d1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
        d1 = data

        newdata =  d1 + relativedelta(hours=quantidade)        
        return newdata

    '''
    parametro:
        data = data que deseja subtrair Exemplo: 2020-03-09
        dias = quantidade de dias que deseja subtrair da tada Exemplo: 7
        resultado = nova data subtraida Exemplo: 2020-03-02
    '''
    @staticmethod
    def subtrairDiasData(data, dias):        
        intervalo = timedelta(dias)
        newdata =  data - intervalo
        
        return newdata

    @staticmethod
    def somarDiasData(data, dias):        
        newdata =  data + timedelta(dias)        
        return newdata

    @staticmethod
    def daterange(start_date, end_date):
        if start_date:
            # WTR - 08/12/2016 INCLUI O +1, POIS Ñ TVA ADD O ULTIMO DIA DO RANGE
            for n in range(int ((end_date - start_date).days+1)):
                yield start_date + timedelta(n)

    @staticmethod
    def timerange(start_time, end_time, qtdMinutes):
        # yield start_time
        
        while end_time > start_time:
            start_time = start_time + timedelta(minutes=qtdMinutes) 
            yield start_time
