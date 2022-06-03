## 1. 웹 크롤링

## 라이브러리 requests(html파일 가져옴), bs4(추출한 html파일 분석)
import requests
from bs4 import BeautifulSoup
import datetime ##시간모듈 오늘 날짜 구하기 위해 사용

현재 = str(datetime.datetime.now())
print(현재)
### 20220602
날 = 현재[:4] + 현재[5:7] + 현재[8:10]
print(날)

req = requests.get("https://school.cbe.go.kr/cw-e/M01030804/list?ymd=" + 날)
#print(req.text) ##웹페이지를 잘 불러왔는지 확인
soup = BeautifulSoup(req.text, "html.parser")
#print(soup)

atag = soup.find("a", href="/cw-e/M01030804/list?ymd=" + 날)
#print(atag)
li = atag.find_all('li')
#print(li)
식단 = ""

for i in li:
    식단 = 식단 + i.text + "\n" #li 태그 안에 있는 글자만 추출하기 위해 text 붙임
#print(식단)



## 2. 텔레그램 봇

# 텔레그램봇 라이브러리 설치 pip install python-telegram-bot

#텔레그램 라이브러리 import해오고 토큰과 봇 정의
import telegram
토큰 = "5464192721:AAEY4vdnft_Si5FyeZcZvhuaqn6cNqsXe3Y"
봇 = telegram.Bot(token=토큰)

#ID가져오기
#for i in 봇.getUpdates():
#    print(i.message)

#앞에서 찾은 ID로 말 걸기
봇.send_message(5394451396, "안녕")

#'안녕'이 아니라 식단 보내보기
봇.send_message(5394451396, 식단)