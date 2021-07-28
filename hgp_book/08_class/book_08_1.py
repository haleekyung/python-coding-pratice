## 딕셔너리로 객체 만들기
students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "윤아란", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92},
]

# 학생 이름 반복하기
print("이름", "총점", "평균", sep="\t")

for student in students:
    score_sum = student["korean"] + student["math"] + \
        student["english"] + student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep="\t")


## 객체를 처리하는 함수(1)
## 딕셔너리 리턴하는 함수로 만들어보기
def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

# 학생 리스트 선언하기
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

# 학생 한명씩 반복하기
print("이름", "총점", "평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] +\
        student["english"] + student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep="\t")


## 객체를 처리하는 함수(2)
def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

# 학생을 처리하는 함수 선언하기
def student_get_sum(student):
    return student["korean"] + student["math"] +\
        student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )

# 학생 리스트 선언
students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

# 학생 호출
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))


## 클래스 선언 방법
class Student:
    pass

## 인스턴스 이름(변수 이름) = 클래스 이름() -> 생성자 함수라고 부름
## 클래스 기반으로 만들어진 객체를 말함

# 학생 선언
student = Student()

# 학생 리스트 선언
student = [
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
    Student(),
]

## 생성자(constructor) : 객체가 생성될 때 내부에 딱 한 번 실행되는 초기화되는 메소드
## 클래스 내부에 __init__ 라는 함수를 만들면, 객체를 생성할 때 처리할 내용을 작성할 수 있음
## self는 '자기자신'을 나타내는 딕셔너리로 생각할 수 있으며, self가 가지는 속성과 기능에 접근할 경우 self.<식별자> 형태로 접근

# 함수 구현
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

# 학생 리스트 선언
student = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
    ]

# Student 인스턴스의 속성에 접근하는 방법
student[0].name
student[0].korean
student[0].math
student[0].english
student[0].science

## 클래스 내부에 함수(메소드) 선언하기
# 클래스 선언하기
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + \
            self.english + self.science

    def average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name, \
            self.get_sum(), \
            self.average())


# 학생 리스트 선언
students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
    ]

# 학생 한 명씩 반복
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student.to_string())