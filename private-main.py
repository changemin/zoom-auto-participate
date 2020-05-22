import webbrowser
from datetime import datetime
import time
import json

with open('private-subjects.json', encoding='utf-8') as subjects_json: # open subject json file
    subjects = json.load(subjects_json)

with open('timetable.json', encoding='utf-8') as timetable_json: # open timetable json file
    timetable = json.load(timetable_json)

weekday = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'] # define weekday
today = weekday[datetime.today().weekday()] # day of week

def printTodaySubjects(): # print today't time table
    print(f'『{today}day time table』')
    for classtime in range(1,timetable[today]["cnt"]+1):
        print(str(classtime) + "교시 : " + timetable[today][str(classtime)])

def meetingURL(meetingID, password): # return meeting link
    url = f'zoommtg://zoom.us/join?action=join&pwd={password}&confno={str(meetingID)}'
    return url

printTodaySubjects()

while(True):
    currnet_time = datetime.now().strftime('%H:%M') # HH:MM
    for classtime in range(1, timetable[today]["cnt"]+1):
        if(currnet_time == timetable["start-time"][str(classtime)]):
            subject = timetable[today][str(classtime)]
            meetingID = subjects[subject]["meetingID"]
            password = subjects[subject]["password"]
            url = meetingURL(meetingID, password)
            webbrowser.open(url)
            print(f'open subject : {subject}')
    # print(f'현재시각 : {currnet_time}')
    time.sleep(60) # 10초마다 검사
