## "from testPackage import *"로
# 모듈을 읽어들일 때 가져올 모듈
__all__ = ["ModuleA", "ModuleB"]

# 패키지를 읽어들일 때 처리를 작성할 수도 잇음
print("testPackage를 읽어들였습니다.")