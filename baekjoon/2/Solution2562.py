## 20210720 - Bronze 2 2562번 문제 최대값 찾기

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
# testcase : 3, 29, 38, 12, 57, 74, 40, 85, 61

numbers = []
for i in range(9):
    number = int(input("자연수를 쓰시오:"))
    numbers.append(number)

print(max(numbers))
print(numbers.index(max(numbers))+1)