import calendar
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta



class DatasUteis():

    @staticmethod
    def convert_date_time_in_datetime(date, time):

        datetimeFormat = '%Y-%m-%d %H:%M'
        time2 = date.strftime('%Y-%m-%d') + ' ' + time.strftime('%H:%M')

        timedelta = datetime.strptime(time2, datetimeFormat) 

        return timedelta

    @staticmethod
    def somarHorasDatetime(data, quantidade, sinal=1):

        # data1 = str(data) + " " + str(hora)
        # d1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
        d1 = data

        if sinal>=1:
            newdata =  d1 + relativedelta(hours=quantidade)        
        else:
            newdata =  d1 - relativedelta(hours=quantidade)        


        return newdata

    @staticmethod
    def somarDiasDatetime(data, quantidade, sinal=1):

        # data1 = str(data) + " " + str(hora)
        # d1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
        d1 = data

        if sinal>=1:
            newdata =  d1 + relativedelta(days=quantidade)        
        else:
            newdata =  d1 - relativedelta(days=quantidade)        


        return newdata

    @staticmethod
    def somarMinutosDatetime(data, quantidade, sinal=1):

        # data1 = str(data) + " " + str(hora)
        # d1 = datetime.strptime(data1, "%Y-%m-%d %H:%M:%S")
        d1 = data

        if sinal>1:
            newdata =  d1 + relativedelta(minutes=quantidade)        
        else:
            newdata =  d1 - relativedelta(minutes=quantidade)        


        return newdata

    @staticmethod
    def last_day_of_month(year, month):
        """ Work out the last day of the month """
        last_days = [31, 30, 29, 28, 27]
        for i in last_days:
            try:
                end = datetime(year, month, i)
            except ValueError:
                continue
            else:
                return end.date()
        return None

    @staticmethod
    def first_day_of_month(year, month):
        """ Work out the last day of the month """
        begin = datetime(year, month, 1)
        return begin.date()

    # @staticmethod
    # def first_day_of_week(year, month, day):
    #     """ Work out the last day of the month """
    #     begin = calendar.calendar(year, month, day)
    #     calendar.setfirstweekday(calendar.MONDAY)
    #     return begin.firstweekday()

    @staticmethod
    def retornaInicioSemana(day):
        day_of_week = day.weekday()

        to_beginning_of_week = timedelta(days=day_of_week)
        beginning_of_week = day - to_beginning_of_week
        print(beginning_of_week)
        print(day)

        to_end_of_week = timedelta(days=6 - day_of_week)
        end_of_week = day + to_end_of_week

        #raise Exception(end_of_week)#hj 2 beginning_of_week=23 end_of_week=

        return (beginning_of_week, end_of_week)



class DiferencaTempo:
    def __init__(self, tempo1, tempo2):
        try:
            self.diff = tempo1 - tempo2
        except:
            tempo1 = DatasUteis.convert_date_time_in_datetime(datetime.now(), tempo1)
            tempo2 = DatasUteis.convert_date_time_in_datetime(datetime.now(), tempo2)
            self.diff = tempo1 - tempo2
        
    def getHoras(self):
        return self.diff.seconds / 3600
        
    def getDias(self):
        return self.diff.days
        
    def getMinutos(self):
        return self.diff.seconds / 60
        
    def getSegundos(self):
        return self.diff.seconds

