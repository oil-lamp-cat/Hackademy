# Python : with 문으로 파일 열기

<aside>
💡 author: 전재호(agamtt), 김가은(circleolami) 2023-12-18

</aside>

with를 이용해서 파일을 읽고 쓸 수 있다.

```python
with expression as variable:
    # 코드 블록
```

기존에는 open(), close()를 이용해서 파일을 읽고 썼다. 

그런데, open() 한 파일을 close()를 하지 않으면 문서가 저장되지 않습니다. 

마치 워드로 문서를 작성하다가 컴퓨터가 꺼지면 작성하던게 모두 날아가는 것과 같습니다.

```python
# example1.py
# Without using with statement
file = open("example.txt", "r")
data = file.read()
print(data)
file.close()
```

근데 코드가 복잡해지면 (파일을 여러개 연다던지) 어떤 파일을 언제 open 했는지 까먹어서 close 를 안하는 경우가 생길 수도 있습니다. 그러면 망하겠죠

파이썬을 이런 문제에 대해서 간편한 방법을 제공합니다.

with 문을 사용하면 open 하고 close 하는 것을 자동으로 까먹지 않고 할 수 있게 해줍니다.

## with 문

with를 사용하면 close()를 하지 않아도 자동으로 닫히기 때문에 데이터 손실이 일어나지 않습니다.

with 문 안에 있는 코드가 모두 실행되면 자동으로 close() 해줍니다.

```python
# example2.py
# Using with statement
with open("example.txt", "r") as file:
    data = file.read()
# File is automatically closed when we exit the with block
```

## 모드

참고로 파일을 여는 모드는 다음과 같습니다.

읽기모드로 열면 편집이 안됩니다.

| 파일 열기 모드 | 내용 |
| --- | --- |
| r | 읽기 모드: 파일 읽기  |
| w | 쓰기 모드: 파일이 존재하지 않으면 새로운 파일 생성, 이미 존재하는 파일이면 기존 내용 삭제 후 쓰기 |
| a | 추가 모드: 파일의 마지막에 새로운 내용 추가 |

## with 문과 소켓

with 문은 소켓에도 사용할 수 있습니다.

소켓도 마찬가지로 연결이 수립된 후 close 하지 않으면 해당 포트를 다른 프로세스가 사용할 수 없습니다.

with 문을 이용하여 소켓을 생성하면 with 문을 빠져나올 때, 해당 포트를 자동으로 해제합니다.

```python
import socket

HOST = 'localhost'
PORT = 12345

# Using with statement to manage socket connection
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, server!')
    data = s.recv(1024)

print('Received:', data.decode('utf-8'))
```

계속