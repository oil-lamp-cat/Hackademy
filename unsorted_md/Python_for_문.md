# Python : for 문

<aside>
💡 author : agamtt 2023-11-29

</aside>

## for

컴퓨터는 인간이 싫어하는 반복적인 일을 하기 위하여 만들어졌습니다.

그래서 모든 프로그래밍 언어와 컴퓨터에는 무언가를 반복하는 기능이 있습니다.

for 는 어떤 코드를 정해진 횟수만큼 반복하는 기능을 수행하는 코드입니다.

for 를 사용하는 코드문장을 for 문이라고 부릅니다.

## Python for문

python 의 for 문은 이렇게 사용합니다.

```python
for i in range(1,100):
	print("Hello!")
```

이 부분은 반드시 똑같아야합니다. 파이썬에서 그렇게 정했습니다. 암기해야합니다.

```python
for ? in range(?,?):
```

그리고 반복하길 원하는 문장은 반드시 들여쓰기 되어있어야 합니다. 들여쓰기는 스페이스바를 네 번 누르거나 Tab 키를 이용하여 입력합니다.

```python
for ? in range(?,?):
	print("hello hacker!")
```

for 문은 range(n,m) 일때 n 부터 m-1 까지 출력합니다.

```python
for i in range(1,5):
	print("hello")

```

즉, 위 코드는 아래와 같습니다.

```python
print("hello") # 첫번째
print("hello") # 두번째
print("hello") # 세번째
print("hello") # 네번째
```

<aside>
💡 **참고**
왜 range(1,5) 인데 5까지 실행안되고 햇갈리게 4에서 끝나나요
>> 그것은 (시작숫자, 이 숫자와 같으면 더이상 실행하지 마세요) 형식이여서 그렇습니다.

</aside>

## 인덱스

for 문에서, for 와 in 사이에 들어가는 저 i 는 사실 변수입니다. 다른 이름으로 해도 무관합니다

```python
for i in range(n,m):
```

```python
for apple in range(n,m): # 바꿔도 정상작동한다.
```

저 i 는 for 문에서만 사용할 수 있으며 for 문을 나가면 더 이상 사용할 수 없습니다.

i 는 for 문이 한 바퀴 돌 때마다 n에서 m 까지 값이 변합니다.

```python
for i in range(1,13):
	print(f"지금은 {i} 바퀴입니다!!!")

print("끝났습니다.")
```

이렇게 for 과 in 사이에 들어가면서, for 문 안에서만 사용할 수 있고 현재의 반복횟수를 저장하고 있는 특수한 변수를 인덱스(index) 라고 부릅니다.

계속