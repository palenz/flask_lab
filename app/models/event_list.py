from app.models.event import Event
import datetime

event1 = Event(datetime.date(2020, 5, 17), "Staff Meeting", 35,  True, 'EDI1', "All staff meeting")
event2 = Event(datetime.date(2020, 6, 18), "1-1 review", 2,  False, 'GLA3', "1-1 Review for weekend Homework")
event3 = Event(datetime.date(2020, 7, 19), "Quiz Night", 40,  False, 'Open Area', "Quiz night for all cohorts")

# def add_new_task(task):
#     tasks.append(task)
