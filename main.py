import webbrowser
from datetime import datetime
import time
import json

weekday = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] # define weekday
today = weekday[datetime.today().weekday()] # day of week

with open('private-subjects.json', encoding='utf-8') as subjects_json: # open subject file
    subjects = json.load(subjects_json)

with open('timetable.json', encoding='utf-8') as timetable_json: # open timetable file
    timetable = json.load(timetable_json)

def printTodaySubjects():
    print('『오늘의 시간표』')
    for classtime in range(1,timetable[today]["cnt"]+1):
        print(str(classtime) + "교시 : " + timetable[today][str(classtime)])
def meetingURL(meetingID, password):
    url = f'zoommtg://zoom.us/join?action=join&pwd={password}&confno={str(meetingID)}'
    return url
# while(True):
# today_timetable = timetable[today]
printTodaySubjects()
print(timetable["start-time"]["4"])
while(True):
    time.sleep(1)
    currnet_time = datetime.now().strftime('%H:%M')
    for classtime in range(1,timetable[today]["cnt"]+1):
        if(currnet_time == timetable["start-time"][str(classtime)]):
            print("hello")
    print(currnet_time + " ... " + timetable["start-time"]["4"])
    if(currnet_time == timetable["start-time"]["4"]):
        print("hello")
