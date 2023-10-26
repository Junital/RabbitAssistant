import datetime

class Event:
    def setStartTime(self, hour, minute):
        self.__starttime = datetime.time(hour, minute)
    
    def setDate(self, year, month, day):
        self.__date = datetime.date(year, month, day)
    
    def setPeriod(self, period):
        """
        Argument:

        period -> Supports int
        """
        self.__period = period
    
    def compareDate(self, date):
        return self.__date == date

    def compareTime(self, time):
        return self.__starttime == time