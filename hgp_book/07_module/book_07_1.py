## url library
## urllib\ module

# 모듈 읽어오기
from urllib import request

# urlopen() 함수로 구글의 메인 페이지 읽어오기
target = request.urlopen("http://google.com")
output = target.read()

# 출력
print(output)