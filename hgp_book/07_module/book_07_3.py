# 모듈 만들기
import TestModule as test

radius = test.numberInput()
print(test.getCercumference(radius))
print(test.getCircleArea(radius))

## 이미지 읽어들이고 저장하기 : 바이너리쓰기 모드 (텍스트데이터.md) 참조
from urllib import request

# urlopen() 함수로 구글의 메인 페이지를 읽어들이기
target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()

print(output)

# write binary[바이너리 쓰기] 모드로
file = open("output.png", "wb") # 바이너리 형식으로 씀
file.write(output)
file.close()
