## 예외처리 종류
### 1. try
* 실행하려고 하는 문장
* except 또는 finally 와 함께하지 않으면 혼자 쓸 수 없음

### 2. except
* 프로그램이 제대로 실행되지 않았을 때 나오는 구문

### 3. else
* 프로그램이 정상적으로 작동되었을 때 나오는 구문

### 4. finally
* 프로그램의 작동여부와 상관없이 마지막에 나오는 구문
* 마지막에 배치

### 예외처리 순서 (꼭 지킬 것)
* try + except 구문 조합
* try + except + else 구문 조합
* try + except + finally 구문 조합
* try + except + else + finally 구문 조합
* try + finally 구문 조합

### 예외처리 안되는 경우
* try + else 구문 조합 : 이 경우는 SyntaxError 발생, 이 경우 아무 실행도 일어나지 않음