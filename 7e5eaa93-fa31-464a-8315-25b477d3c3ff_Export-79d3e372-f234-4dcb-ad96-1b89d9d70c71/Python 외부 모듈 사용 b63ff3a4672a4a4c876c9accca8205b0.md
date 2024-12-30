# Python : 외부 모듈 사용

<aside>
💡 author : agamtt 2023-11-30

</aside>

### import

python 에서는 다른 py 파일을 현재 py 파일에 포함시켜서 실행시킬 수 있습니다.

이렇게 불러온 다른 파일을 모듈(module)이라고 부릅니다.

주로 다른 파일에 있는 함수를 사용하기위해 사용합니다.

한 폴더에 아래와 같은 파일 두개를 만듭니다.

```python
# hello.py

def sayhello():
    print("Hello, this is hello.py!")
```

```python
# myprogram.py

import hello

hello.sayhello()
```

import hello 로, .py 확장자를 제외한 파일이름을 입력하면 해당 파일이 불러와집니다.

myprogram.py 를 python 으로 작동시키면 hello.py 안의 함수가 실행됩니다.

만일 myprogram.py 에 sayhello() 가 이미 선언된 경우, hello.sayhello() 는 hello.py 에서 선언된 함수를 의미하고, sayhello() 는 myprogram.py 의 sayhello() 를 의미합니다.

```python
# hello.py

def sayhello():
    print("Hello, this is hello.py!")
```

```python
# myprogram.py

import hello

def sayhello():
    print("Hello, this is sayhello() in myprogram!")

hello.sayhello()
```

## from import

불러오려는 파이썬 파일이 큰 경우, 불러오는데 오래걸릴 수도 있습니다.

또한 안에 포함된 함수가 많은 경우, 어떤 함수를 사용했는지 나중에 알아보기가 힘듭니다.

from 을 사용하면 불러오려는 파일에서 특정 함수만 불러올 수 있습니다.

```python
# hello.py

def sayhello():
    print("Hello, this is hello.py!")

def saybabo():
    print("Hello, this is hello.py!")

def add(a,b):
		print(a+b)
```

```python
# myprogram.py

from hello import saybabo

saybabo()
```

아래 코드는 오류를 일으킵니다. saybabo 만 불러왔기 때문에 sayhello 를 찾을 수 없습니다. 

```python
# myprogram.py

from hello import saybabo

sayhello()
```

또한, from 으로 불러오면 앞에 불러온 모듈이름을 붙이지 않아도 됩니다.

## 모두 불러오기

*, 그러니까 별 기호는 애스터리스크(Asterisk) 라고 불립니다.

별 기호는 컴퓨터에서 “모든” 을 의미합니다.

import * 을 사용하면 해당 모듈의 모든 함수를 불러옵니다.

그러면 import {{module_name}} 과 달리 해당 모듈의 모든 함수를 모듈이름을 앞에 붙이지 않고 사용할 수 있습니다.

하지만 추천되는 방법은 아닙니다. 함수이름이 충돌할 수도 있습니다. (동일한 함수명이 존재하는 경우)

```python
# myprogram.py

from hello import *

sayhello()
```

계속