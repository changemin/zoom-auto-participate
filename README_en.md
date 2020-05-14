# Zoom Meeting Auto Participate

from now on, you don't need to enter password to each meetings

it provides your break time

all of json data is korean, but don't be afraid of it. just following the usage introduction bellow. and replace it into your language

## 🚨Caution
    this program doesn't ask you to participate the meeting or not. 

    subject name should be 100% same between time-table.json and subjects.json

## 🌴 Usage

### 1. Clone this repository to you local storage
    WORKSPACE:> git clone https://github.com/Changemin/zoom-auto-participate.git
 
### 2. modify time-table.json
from monday(mon) to friday(fri)

example :
```
"mon":{
    "1" : "English",
    "2" : "P.E.",
    "3" : "Math",
    "4" : "Spainish",
    "5" : "Biology",
    "6" : "Life",
    "7" : "Dance Class",
    "cnt" : 7
}

...

"fri":{
    ...
}
```

### 3. modify subjects.json
nomally, you can get the meetingID via way you participate the meeting before

example : 
```
"subject name":{
    "meetingID":(meeting ID),
    "password":"(password)"
}
```
### 4. run it! and get some rest :D
    WORKSPACE:> cd zoom-auto-participate
    WORKSPACE:> python3 main.py