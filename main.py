import webbrowser
from datetime import *
import time
import json

weekday = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] # define weekday
today = weekday[datetime.today().weekday()] # day of week

with open('private-subjects.json') as subjects_json: # open subject file
    subjects = json.load(subjects_json)

with open('timetable.json') as timetable_json: # open timetable file
    timetable = json.load(timetable_json)

while(True):


def printTodaySubjects():
    for day in range(1,7):
    print(subjects[today][str(day)])