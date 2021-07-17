# ## 예외 처리하기 - 조건문
# ## 사용자가 정수를 넣어햐 할 곳에 문자열을 넣었을 때
#
# # 숫자 입력받기
# user_input_a = input("정수 입력: ")
#
# # 사용자 입력이 숫자로만 구성되어 있을 경우
# if user_input_a.isdigit():
#     number_input_a = int(user_input_a)
#     print("원의 반지름: ", number_input_a)
#     print("원의 둘레: ", 2 * 3.14 * number_input_a)
#     print("원의 넓이: ", 3.14 * number_input_a ** 2)
#
# else:
#     print("정수를 입력하지 않았습니다")


## 어떤 부분에서 예외가 발생하는 지 대략 알 수 있는 경우
## except 구문에 아무것도 넣지 않고 try 구문 사용
## 구문 내부에 아무것도 넣지 않으면 구문 오류가 발생하므로, 다음과 같이 pass 키워드를 사용

# try:
    # 예외가 발생할 가능성이 있는 코드
# except:
    # pass


# ## 실습해보기
# # 변수 선언하기
# list_input_a = ["52", "273", "32", "스파이", "103"]
#
# # 반복 적용하기
# list_number = []
# for item in list_input_a:
#     try:
#         float(item) # 예외가 발생하면 알아서 다음으로 진행은 안되겠지?
#         list_number.append(item) # 예외없이 통과했으면 리스트에 넣어줄것
#
#     except:
#         pass
#
# # 출력하기
# print("{} 내부에 있는 숫자는".format(list_input_a))
# print("{} 입니다.".format(list_number))
#

## try except else 구문
## 예외가 발생하지 않았을 때 실행할 코드를 지정할 수 있다.

# try:
    # 예외가 발생할 가능성이 있는 코드

# except:
    # 예외가 발생했을 때 실행할 코드

# else:
    # 예외가 발생하지 않았을 때 실행할 코드


# # try except else 구문으로 예외처리하기
# try:
#     number_input_a = int(input("정수를 입력하시오: "))
#
# except:
#     print("정수를 입력하지 않았습니다")
#
# else:
#     print("원의 반지름 길이: ", number_input_a)
#     print("원의 둘레: ", number_input_a * 2 * 3.14)
#     print("원의 넓이: ", number_input_a ** 2 * 3.14)

## finally 구문
## 예외가 발생하든 발생하지 않든, 무조건 실행할 때 사용

# try:
#     number_input_a = int(input("정수를 입력하시오: "))
#     print("원의 반지름 길이: ", number_input_a)
#     print("원의 둘레: ", number_input_a * 2 * 3.14)
#     print("원의 넓이: ", number_input_a ** 2 * 3.14)
#
# except:
#     print("정수를 입력하지 않았습니다")
#
# else:
#     print("예외가 발생하지 않았습니다.")
#
# finally:
#     print("어떻게든 끝났습니다.")
#
# ## 파일이 제대로 닫혔는지 확인해보기
# # try except 구문 사용하기
# try:
#     file = open("info.txt", "w")
#     file.close()
# except Exception as e:
#     print(e)
#
# print("파일이 제대로 닫혔는지 확인하기")
# print("file.closed: ", file.closed)


# ## 오류가 나는 구문
# try:
#     file = open("info.txt", "w")
#     예외.발생해라()
#     file.close()
# except Exception as e:
#     print(e)
#
# print("파일이 제대로 닫혔는지 확인하기")
# print("file.closed: ", file.closed)
#
# ## -> 이ㄷ 때 closed가 False로 파일이 닫히지 않는다는 것을 확인할 수 있어, 반드시 finally 구문을 활용해 닫아야 함

## 오류 수정 -> finally 구문 추가하기
# try:
#     file = open("info.txt", "w")
#     예외.발생해라()
#     file.close()
# except Exception as e:
#     print(e)
#
# finally:
#     file.close()
#
# print("파일이 제대로 닫혔는지 확인하기")
# print("file.closed: ", file.closed)
#
# ## -> 이 때 closed가 False로 파일이 닫히지 않는다는 것을 확인할 수 있어, 반드시 finally 구문을 활용해 닫아야 함

## try 구문 내부에서 return 키워드를 사용하는 경우
# test() 함수를 선언하기
def test():
    print("test() 함수의 첫줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문이 return 키워드 뒤입니다.")

    except:
        print("except 구문이 실행되었습니다.")

    else:
        print("else 구문이 실행되었습니다.")

    finally:
        print("finally 구문이 실행되었습니다.")

test()
