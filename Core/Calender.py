import json
import datetime
from Core.Event import Event


class Calendar:
    def __init__(self):
        self.__eventlist = []

    def addEvent(self, event):
        self.__eventlist.append(event)
    
    def delEvent(self, event):
        self.__eventlist.remove(event)
    
    def changeEvent(self, oldevent, newevent):
        self.delEvent(oldevent)
        self.addEvent(newevent)

    def show_day(self, date):
        ans_list = []
        for event in self.__eventlist:
            if(event.compareDate(date)):
                ans_list.append(event)
        return ans_list