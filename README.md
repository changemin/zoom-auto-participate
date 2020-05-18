👉 [English](README_en.md) 

# Zoom Meeting Auto Participate
아니 학교에 있으면 쌤들이 교실로 오는데 이건 뭐 내가 쉬는시간마다 교실을 찾아가야하는 꼴이 되어버리니 이렇게 귀찮을 수가 없다 아니 그리고 비밀번호까지 쳐야되잖아

## 🚨주의사항
    회의 참가할땐 따로 물어보지 않으니까 조심조심,,
    근데 카메라를 킬건지 클건지는 물어본다

    time-table.json 과 subjects.json에 있는 수업 이름이 동일해야한다

## 🌴시작하기

### 1. repository를 로컬저장소로 복사하기
    WORKSPACE:> git clone https://github.com/Changemin/zoom-auto-participate.git
 
### 2. time-table.json을 자신에게 맞는 시간표로 수정하기
월요일부터 금요일까지, 1교시 부터 7교시(또는 6교시)

예시 :
```
"mon":{
    "1" : "영어",
    "2" : "응용프로그래밍개발",
    "3" : "문학",
    "4" : "물리학",
    "5" : "중국어",
    "6" : "성공적인직업생활",
    "7" : "공업수학",
    "cnt" : 7
}

...

"fri":{
    ...
}
```

### 3. subjects.json을 알맞는 과목별 회의 ID와 비밀번호로 수정하기
디미고 기본적으로 추가되어있습니당( 비밀번호는 입력해야함. )
순서는 상관 없고 다음과 같은 포맷만 맞추어서 추가해주세요
회의 아이디는 보통 학교에서 안내해준 링크 url안에 있어요!

예시 : 
```
"과목이름":{
    "meetingID":(회의 참가 ID),
    "password":"(비밀번호)"
}
```
### 4. 실행하고 편하게 쉬자 !
    WORKSPACE:> cd zoom-auto-participate
    WORKSPACE:> python3 main.py

## 🔥추가할 기능들

* 조례 및 종례 자동참가
* command 로 참가
* 회의 자동참가시 알림(소리 등)

    
    
