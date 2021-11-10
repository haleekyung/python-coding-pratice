### 클래스의 추가적인 구문
## 어떤 클래스의 인스턴스인지 확인해보기 - isinstance()
## isinstance(인스턴스, 클래스): 인스턴스가 해당 클래스를 기반으로 만들어졌을 경우에는 True, 전혀 상관이 없는 인스턴스와 클래스라면 False를 리턴

# 클래스 선언하기
class Student:
    def __init__(self):
        pass

# 학생을 선언하기
student = Student()

# 인스턴스 확인하기
print("isinstance(student, Student): ", isinstance(student, Student)) # 맞기 떄문에 True로 출력할것

## 단순한 인스턴스 확인해보기
type(student) == Student

## isinstance() 활용해보기
# 학생 클래스 선언하기
class Student:
    def study(self):
        print("학생입니다.")

# 선생님 클래스 선언하기
class Teacher:
    def teach(self):
        print("선생님입니다.")

# 리스트를 사용하기
classroom = [Student(), Student(), Teacher(), Teacher(), Student(), Student()]

# 반복문 사용하기
for person in classroom:
    if isinstance(person, Student):
        person.study()

    elif isinstance(person, Teacher):
        person.teach()

## __str__() 함수 정의하여 클래스 내부에서 사용하기
# 클래스를 선언하기
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self): # 객체를 문자열로 변환할 수 있음
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average())

    def __eq__(self, value):
        return self.get_sum() == value.get_sum()

    def __ne__(self, value):
        return self.get_sum() != value.get_sum()

    def __gt__(self, value):
        return self.get_sum() > value.get_sum()

    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()

    def __lt__(self, value):
        return self.get_sum() < value.get_sum()

    def __le__(self, value):
        return self.get_sum() <= value.get_sum()


# 학생 리스트를 선언하기
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
]

# 학생 선언하기
student_a = Student("윤인성", 98, 98, 88, 95),
student_b = Student("연하진", 92, 98, 96, 98),

# 출력하기
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))

# 출력하기(2) : 학생 성적 비교
print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)

## TypeError 발생시키기 : 다른 자료형과 비교할 때에도 현재는 마찬가지이므로, 사용되는 자료형을 한정시키고 싶을 경우 TypeError 발생시켜줄것
# 클래스 선언하기
class Student:
    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 사용할 수 있습니다.")
        return self.get_sum() == value.get_sum()


# 학생 선언하기
student_a = Student("윤인성, 87, 98, 88, 95")

# 학생 비교하기
student_a == 10


## 클래스 변수
# 클래스 선언하기
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        # 인스턴스 변수 초기화하기
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))


# 학생 리스트를 선언하기
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

# 출력
print()
print("현재 생성된 학생 수는 {}명입니다.".format(Student.count))

# 함수를 이용한 데코레이터
def hello():
    print("hello")

# 위 코드 앞에 "인사가 시작되었습니다." 뒤에 "인사가 종료되었습니다."를 출력하고 싶은 경우
# 아래의 코드를 예제로 구현함

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

# 함수 호출하기
hello()

## 클래스 함수
# 클래스 선언하기
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("---- 학생 목록 ----")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("----------------")

    # 인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    @property
    def __str__(self):
        return("{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average()))


# 학생 리스트 선언하기
Student("윤인성", 87, 98, 88, 95),
Student("연하진", 92, 98, 96, 98),
Student("구지연", 76, 96, 94, 90),
Student("나선주", 98, 92, 96, 92),
Student("윤아린", 95, 98, 98, 98),
Student("윤명월", 64, 88, 92, 92),
Student("김미화", 82, 86, 98, 88),
Student("김연화", 88, 74, 78, 92),
Student("박아현", 97, 92, 88, 95),
Student("서준서", 45, 52, 72, 78)

# 현재 생성된 학생 모두 출력하기
Student.print()