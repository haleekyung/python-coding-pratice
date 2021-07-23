# main.py 파일

print("# 메인의 __name__ 출력하기")
print(__name__)
print()


import TestPackage.ModuleA as a

print(a.variableA)
print(a.variableB)