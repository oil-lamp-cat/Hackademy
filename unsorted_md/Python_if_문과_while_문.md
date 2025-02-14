# Python : if 문과 while 문

<aside>
💡 author : agamtt 2023-11-29

</aside>

### if 문

컴퓨터 프로그램은 특정 상황에서만 작동하도록 만들어야할 때가 있습니다.

시한폭탄을 코딩한다고 가정해봅시다. 

시한폭탄은 숫자가 계속 줄어들다가, 숫자가 0이 되면 폭발해야합니다.

이러한 기능을 코딩에서는 if 문을 이용하여 코딩합니다.

if 는 영어로 “만약”이라는 뜻입니다.

if 문은 만약~ 라면 실행한다 라는 상황을 코딩하는데에 쓰입니다.

```python
if(시간이 0이 되면):
	boom # 폭탄이 터지는 코드
```

if 문의 괄호 안에는 True 또는 False 로 계산될 수 있는 값이 들어갑니다.

등호 연산자 == 을 사용하면 값이 같은지 다른지에 따라 True 와 False 로 변합니다.

다음은 행운의 숫자를 찾는 코드입니다.

```python
a = 7

if(a==7):
	print("this is lucky number seven!")
print("end!!")
```

만일 행운의 숫자인 7이 아닌 다른 값을 넣는다면 실행되지 않습니다.

```python
a = 9

if(a==7):
		print("this is lucky number seven!")
print("end!!")
```

if 문이 거짓이므로 if 문 안에있는 코드는 실행되지 않습니다.

그러나 if문이 거짓이건 참이건 if문 밖에 있는 코드는 실행됩니다. 따라서 end!! 는 if문과 무관하게 출력됩니다.

if 문에는 > 와 < 로 크기를 검사하게 할 수 있습니다. 이 둘을 부등호 연산자라고 부릅니다

```python
age = 10
if(a>20):
	print("you are adult!")
```

## else 와 elif

else 는 if 와 같이 쓰여서, “나머지 조건” 에 실행되도록 합니다.

else 는 영어로 “그렇지않으면” 이라는 뜻 입니다.

else 문은 만약~면 ~하고, 그렇지않으면 ~한다 라는 코드를 만들때 쓰입니다.

```python
a = 9
if(a==7):
	print("this is lucky number seven!")
else:
	print("this is not seven, you babo!")
```

이렇게 작성하면, if 를 만나면 a를 7과 비교한 뒤 7이면 if 문을 실행하고 7이 아니면 else 문을 실행합니다.

이렇게 바꿔서 실행해보세요.

```python
a = 7
if(a==7):
	print("this is lucky number seven!")
else:
	print("this is not seven, you babo!")
```

elif 는 else if 의 약자로, ~또, ~라면 라는 뜻 입니다.

elif 문은 if 문으로 여러개의 조건을 검사하고 싶을때 쓰입니다. 예를 들어, 아래 코드는 4는 불길한 숫자, 7은 행운의 숫자, 나머지 숫자는 i don’t care를 출력하는 코드입니다.

```python
num = 5
if(a==7):
	print("this is lucky number seven!")
elif(a==4):
	print("shittt! this is unlucky number four!")
else:
	print("this is nothing... i dont care")
```

## while

while 문은 ~동안 이라는 뜻입니다.

while 문은 괄호안의 값이 True인지 False 인지 검사하고, True 이면 다시 while 문의 처음으로 돌아옵니다. 즉, false 가 되지 않는 한 무한으로 실행됩니다.

```python
while(True):
	print("hello!")
```

while 문에 항상 True 인 값을 넣는 경우, 무한루프에 빠져서 프로그램이 종료되지 않습니다.

터미널에서는 X키나 홈버튼을 눌러서 프로그램을 끌 수 없으므로 Ctrl+c 를 누르면 됩니다.

while 문의 조건은 무한루프에 빠지지 않도록 어떨 때에는 참이고 어떨 때에는 거짓이 나오도록 해야합니다.

while 을 for 문 처럼 쓸 수도 있습니다. 아래 코드는 10번만 실행됩니다.

a가 0 일때 실행되고 a에 1을 더하고, 1일때 실행되고 a에 1을 더하고, 2일때 실행되고 a에 1을 더하고 …

a 가 10일때는 a<10 이 거짓이므로 실행되지 않습니다

따라서 0~9 , 10번 실행됩니다.

```python
a=0
while(a<10):
	print("kgu baboo!!!!")
	a+=1
```

## while 과 if 로 시한폭탄 만들기

당신이 해커인데, 시한폭탄을 프로그래밍 한다고 해봅시다.

물론 폭발하는 부분은 화학공학과 학생이 만들어주었습니다.

시한폭탄은 다음의 기능을 해야합니다.

- 숫자를 셉니다. 숫자는 1씩 줄어듭니다.
- 폭탄 표시장치에 숫자를 계속 표시해야합니다.
- 숫자가 0 보다 작으면 폭발해야합니다.

```python
timer = 6000

while(True):
	print(f"{timer} second left.")
	timer -= 1
	if(timer<0):
		print("BooMMM !!!!!!")
```

계속