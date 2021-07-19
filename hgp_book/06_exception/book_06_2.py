## 예외 객체
## Exception : 클래스

# try except 구문으로 예외 처리하기
try:
    # 숫자로 변환하기
    number_input_a = int(input("정수 입력: "))
    # 출력하기
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", number_input_a * 3.14 * 2)
    print("원의 넓이: ", number_input_a ** 2 * 3.14)

except Exception as exception:
    # 예외 객체를 출력해보기
    print("type(exception): ", type(exception))
    print("exception: ", exception)


## 변수를 선언합니다.
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외 처리하기
try:
    number_input = int(input("숫자를 입력하시오: "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))

except Exception as exception:
    print("type(exception): ", type(exception))
    print("exception: ", exception)

# 변수를 생성하기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력: "))
    print("{}번쨰 요소: {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()

except ValueError as exception:
    print("정수를 입력해 주세요.")
    print("exception: ", exception)

except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception: ", exception)

except Exception as exception:
    print("파악하지 못한 예외가 나타났습니다.")
    print("exception: ", exception)


## 예외 강제로 발생시키기 : raise 구문
# 입력 받기
number = input("정수 입력: ")
number = int(number)

# 조건문 사용
if number > 0:
    # 양수일 때 : 아직 미구현 상태임
    raise NotImplementedError

else:
    # 음수일 때 : 아직 미구현 상태임
    raise NotImplementedError