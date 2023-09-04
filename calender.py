import json
import datetime

class Calendar:
    def add_event(self):
        pass

    def show_day(self, date):
        event_list = []

        with open('data/{date}.json', 'r') as f:
            data = json.load(f)
            event_list.append(data)

        return event_list

    def display(self):
        today = datetime.date.today()
        today_event = self.show_day(today)

        plus_1_day = today + datetime.timedelta(days=1)
        plus_1_day_event = self.show_day(plus_1_day)

        puls_2_day = today + datetime.timedelta(days=2)
        puls_2_day_event = self.show_day(puls_2_day)

        minus_1_day = today - datetime.timedelta(days=1)
        minus_1_day_event = self.show_day(minus_1_day)

        minus_2_day = today - datetime.timedelta(days=2)
        minus_2_day_event = self.show_day(minus_2_day)

        print(minus_2_day.ljust(30), minus_1_day.ljust(30), today.ljust(30), plus_1_day.ljust(30), puls_2_day)

    
Calendar.display()