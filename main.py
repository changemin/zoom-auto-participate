import webbrowser
from datetime import *
import time
import json

weekday = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] # define weekday
today = weekday[datetime.today().weekday()] # day of week

with open('private-subjects.json', encoding='utf-8') as subjects_json: # open subject file
    subjects = json.load(subjects_json)

with open('timetable.json', encoding='utf-8') as timetable_json: # open timetable file
    timetable = json.load(timetable_json)

# while(True):
today_timetable = timetable[today]
print(today_timetable)

def printTodaySubjects():
    for day in range(1,7):
        print(timetable[today][str(day)])