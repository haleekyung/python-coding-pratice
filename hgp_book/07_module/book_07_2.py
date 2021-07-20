## 외부 모듈
## 다른 사람이 만들어 배포하는 모듈을 '외부 모듈(External Module)'이라고 한다.
## 예시) Beautiful soup, Flask

# 모듈 불러오기
from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수를 이용해 기상청의 전국 날씨 가져오기
target = request.urlopen("https://www.weather.go.kr/w/weather/forecast/mid-term.do?stnId1=109")

# BeautifulSoup을 사용해 웹페이지 분석하기
soup = BeautifulSoup(target, "html.parser")

# location 태그를 찾습니다.
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아서 출력하기
    print("도시: ", location.select_one("city").string)
    print("날씨: ", location.select_one("wf").string)
    print("최저기온: ", location.select_one("tmn").string)
    print("최고기온: ", location.select_one("tmx").string)

## Flask로 웹 서버 만들기
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

set FLASK_APP = hello_world.py
flask run

## 함수 데코레이터
def hello():
    print("hello")

def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

# 데코레이터를 붙여 함수 만들기
@test
def hello():
    print("hello")

hello()
