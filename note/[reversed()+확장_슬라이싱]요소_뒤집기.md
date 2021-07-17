## 리스트 내부에 있는 요소를 뒤집고 싶을 때
### 1. reversed() 함수 사용하기
```{.python}
    numbers = [1, 2, 3, 4, 5]
    
    for i in reversed(numbers):
        print("첫번째 반복문: {}".format(i))
```

### 2. 확장 슬라이싱 사용하기: [::-1]
```{.python}
    >>> numbers = [1, 2, 3, 4, 5]
    >>> numbers
    [1, 2, 3, 4, 5]
    
    >>> numbers[::-1]
    [5, 4, 3, 2, 1]
```

