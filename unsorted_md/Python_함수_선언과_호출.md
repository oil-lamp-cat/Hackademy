# Python : 함수 선언과 호출

<aside>
💡 author : agamtt 2023-11-29

</aside>

## 함수

함수는 코딩하는 사람이 어떤 코드를 약간만 바꿔서 여러 번 써야 할 때를 위해서 만들어졌습니다.

함수는 쓰기 전에 만들어야 합니다. 코딩에서 함수를 만드는 것을 선언한다(define)고 합니다.

- 함수 안에는 들여쓰기로 함수가 실행될 때 작동할 코드를 적습니다.
- def 는 define(선언)의 약자로, def 가 나오면 파이썬은 뒤에 함수를 선언할 것이라고 생각합니다.
    - 그래서 def 라는 이름의 변수는 쓸 수 없습니다.
- 함수 이름 뒤에는 괄호가 나옵니다.

```python
def function_name():
	print("Hello Hacker!")
```

이렇게 하면 함수가 만들어집니다.

이 함수를 쓰려면 함수이름 뒤에 괄호를 붙이면 됩니다.

이미 선언된 함수를 사용하는 것을 함수를 호출(call)한다고 합니다.

아래는 sayhello 라는 함수를 만들고 호출합니다.

```python
def sayhello():
	print("hello!!!")

sayhello()
```

### 인자, 매개변수(parameter, argument)

함수가 정말 똑같은 동작을 반복한다면 사실 그냥 코드를 복붙하면 됩니다.

하지만 함수는 변수를 만들어서 실행할 때, 그 변수를 정해서 실행하도록 할 수 있습니다.

이를 매개변수라고 부릅니다.

아래 코드는 a와 b를 매개변ㅁ수로 입력 받아서 a+b 를 더한 것을 출력하는 함수를 선언합니다.

```python
def add(a,b):
	sum = a+b
	print(sum)
```

함수를 만들면 사용할 수 있습니다.

아래는 함수를 선언하고 사용하는 코드입니다.

```python
def add(a,b):
	sum = a+b
	print(sum)

add(2,3)
add(177,249)
add(123919,12313)
```

함수의 매개변수로 변수를 집어넣을수도있습니다.

```python
def add(a,b):
	sum = a+b
	print(sum)

num1 = 17
num2 = 29

add(num1,num2)
```

## return (반환)

함수는 함수를 실행하고서 나온 값을 밖으로 내놓을 수 있습니다.

이를 반환(return) 이라고 부릅니다.

아래는 위의 add 함수를 변형한 것 인데, 함수 안에서 print 하는 것이 아니라, 값을 반환합니다.

```python
def add(a,b):
	sum = a+b
	return sum

add(2,3) # 출력되지 않습니다.
print(add(2,3)) # 출력됩니다.
```

이렇게 반환하는 값을 가진 함수는 쓸모가 많습니다. 예를 들어, 함수의 return 값은 다른 연산에 다시 쓰이거나 변수에 저장될 수 있습니다.

```python
def add(a,b):
	sum = a+b
	return sum

sum_of_three_five = add(3,4)
sum_of_seven_thirteen = add(7,13)

sum_of_three_five_seven_thirteen = add(sum_of_three_five,sum_of_seven_thirteen)
```

### 함수를 쓰면 코드 재사용에 좋음

함수를 쓰면 똑같은 코드를 다시 쓸 때 편리합니다.

예를 들어 다른 사람에게 이름을 불러주며 인사를 하는 코드를 만들어 봅시다.

```python
print("hello john!")
```

하지만 jeho 에게 인사하려면 john 대신 jeho 를 넣어서 다시 써야합니다.

```python
print("hello jeho!")
```

이처럼 코드를 다시 사용해야하는 상황을 “코드 재사용” 이라고 부릅니다. 이런 상황에서 함수를 쓰는 것이 도움이 됩니다.

원주율을 계산하는 코드를 작성한다면, 이렇게 써야합니다. 뭐 원주율 정도는 공식을 다 아니까 그냥 코드를 작성해도 됩니다.

```python
3.14 * radius ** 2
```

그러나 루트 2, 즉 2의 제곱근을 구하는 코드는 아래와 같습니다.

```python
guess = x / 2
    for _ in range(100):
        guess = (guess + x / guess) / 2
```

이러한 코드는 코드만 보고서는 대체 무슨 동작을 하는 것인지 쉽사리 추측하기 힘듭니다.

하지만 만일 이를 함수로 만든다면, 내 코드를 다른사람이 사용하게 되었을때, 함수이름만 보고 어떻게 사용하는지 쉽게 알 수 있습니다.

아래는 제곱근을 계산하는 함수를 선언하는 코드입니다.

```python
def calculate_square_root(x, num_iterations=100):
    guess = x / 2
    for _ in range(num_iterations):
        guess = (guess + x / guess) / 2
    return guess
```

이와 같은 함수를 선언해놓으면, 나중에 제곱근을 계산할때 편리합니다.

함수가 어떻게 코딩되어있는지 몰라도, 숫자를 넣으면 제곱근값이 나온다는 것만 알면 사용할 수 있습니다.

```python
def calculate_square_root(x, num_iterations=100):
    guess = x / 2
    for _ in range(num_iterations):
        guess = (guess + x / guess) / 2
    return guess

x = 16
result = calculate_square_root(x)
print(f"Square root of {x} is approximately {result}")

y = 36
result = calculate_square_root(y)
print(f"Square root of {x} is approximately {result}")
```

이를 추상화(abstraction) 이라고 부릅니다. 코드에는 다양한 추상화 방법이 있습니다. 함수는 코드를 추상화하는 방법중 하나입니다.

계속