# 컨테이너 두개로 python socket 실습

<aside>
💡 author : agamtt 2023-11-30

</aside>

# 실습 환경 만들기

<aside>
💡 **여기를 참고합니다.**

[실습 : 컨테이너 두개 만들고 포트포워딩하기](%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%B3%E1%86%B8%20%E1%84%8F%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%82%E1%85%A5%20%E1%84%83%E1%85%AE%E1%84%80%E1%85%A2%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%A9%20%E1%84%91%E1%85%A9%E1%84%90%E1%85%B3%E1%84%91%E1%85%A9%E1%84%8B%E1%85%AF%E1%84%83%E1%85%B5%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20995d9cf49347438e9eaa9ecc47cac664.md)

</aside>

파이썬으로 socket 을 생성하고 port 번호를 받아서 네트워크에 연결할 수 있습니다.

<aside>
💡 소켓 통신 코드는 형식이 정해져있어서 복붙해서 사용하면 됩니다.
네트워크 통신을 하는 프로그램의 모든 코드라면 무조건 포함하고 있습니다.

</aside>

우선 client 와 server 에 둘 다 python3 를 설치합니다.

```bash
apt update
apt install python3
```

socket 은 python 에 이미 기본 모듈로 제공됩니다. 

socket.py 라는 파일이 python3 가 다운로드될때 같이 다운로드됩니다.

import 하기만 하면 됩니다.

send.py 를 만들고 아래와 같이 작성합니다.

```python
# send.py - client에 작성하기 
import socket

print("send start...")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((target_host, target_port))

data_to_send = b"Hello!\n"
client_socket.send(data_to_send)

exit()
```

위 프로그램은 파이썬으로 소켓을 생성하고 IP주소와 입력된 port 로 데이터를 전송합니다. 

아랫부분은 socket 모듈에 포함되어있는 함수로, Python 공식문서를 찾아보면 사용법이 나옵니다.

socket.socket() 함수는 소켓을 생성합니다. AF_INET 은 인터넷 연결을 사용하겠다는 매개변수이고, SOCK_STREAM은 한번 연결이 수립되면 계속 통신할 수 있게 하는 TCP 연결을 사용하겠다는 매개변수입니다.

```python
socket.socket(socket.AF_INET,socket.SOCK_STREAM)
```

이 파이썬 코드는 보내는 쪽이므로, 편지나 택배에 주소를 적는 것 처럼 실제 연결하려는 컴퓨터의 host 와 port 를 입력해야합니다.

```python
client_socket.connect((target_host, target_port))
```

문자열을 보낼때에는 b 를 앞에 붙여서 바이너리로 바꿔야합니다.

바이너리로 바꿔야 소켓을 통해 보낼 수 있습니다.

\n 은 줄바꿈, 즉 엔터를 의미합니다.

```python
data_to_send = b"Hello!\n"
```

# Python Socket 으로 전송하고 nc 로 받기

실제 접속 정보를 이용해서

ifconfig 로 확인한 접속정보는 아래와 같습니다.

```
client ip : 172.17.0.3
client port : 8002

server ip : 172.17.0.2
server port : 8001
```

따라서 코드를 아래와 같이 수정합니다.

client 에 저장된 py 파일입니다.

```python
import socket

print("send start...")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("172.17.0.2", 8001))

data_to_send = b"Hello!\n"
client_socket.send(data_to_send)

exit()
```

실행해보면 접속이 거절되었다고 나옵니다. 전에 배운 것 처럼, 서버쪽에서도 Listen 대기하고 있어야합니다.

(접속이 거절되지 않았는데, 통신이 안된다면, 해당 포트를 이미 사용중인 프로세스가 있어서 그런 것일 수 있습니다. 포트를 바꿔보세요)

![Untitled](Untitled%20232.png)

서버에서 다음의 명령어를 실행하여 nc 로 python 이 보낸 패킷을 확인합니다.

```python
nc -l -p {나의 port}
```

저의 접속정보에 의하면 서버의 port 는 8001 이니, 아래와 같이 입력합니다.

파이썬 코드를 실행하기 전에, server에서 nc명령어를 먼저 치셔야 합니다!

(nc~~ 쳤더니 뭔가 커서만 대기(?)하고 있으면 성공입니다.)

```python
nc -l -p 8001
```

아래와 같이 입력하면 성공합니다.

![Untitled](Untitled%20233.png)

# nc 로 전송하고 Python Socket 로 받기

python 코드를 이용하여 소켓을 생성하고 listen 하는 것은 socket.bind 함수로 가능합니다.

recieve 를 의미하는 recv.py 를 만들고 다음과 같이 작성합니다.

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Listening ...")

client_socket, client_address = server_socket.accept()
print("Connection Accepted!")

data = client_socket.recv(1024)

print(f"Received data: {data.decode('utf-8')}")
client_socket.close()
```

아래 코드는 소켓을 특정 포트에 “바인드” 합니다. 그러면 소켓이 포트에 연결됩니다.

해당 포트로 들어오는 통신은 모두 이 소켓이 가져가게 됩니다.

```python
server_socket.bind((host, port))
```

listen(1) 은 한명만 줄세우겠다는 말입니다. 어려운말로 대기큐라고 부릅니다.

```python
listen(1)
```

다른 컴퓨터가 있어서 연결을 요청하면 그 컴퓨터까지는 대기시키고, 이전 연결이 끊어지면 연결해줍니다.

하지만 컴퓨터가 잔뜩 줄서있으면 불편하니, 2번째 줄서있는 컴퓨터부터는 줄을 못서게 그냥 거절합니다. (그럼 해당 컴퓨터에서는 에러가 뜨겠지요?)

아래 코드는 1024 바이트만큼의 데이터를 전송받은 후 이를 utf-8 이라는 포맷으로 출력합니다.

```python
data = client_socket.recv(1024)

print(f"Received data: {data.decode('utf-8')}")
```

socket.close() 는 연결을 중지시킵니다.

```python
client_socket.close()
```

실제로 접속해보겠습니다.

접속정보는 아래와 같습니다. (본인의 컴퓨터에서 ifconfig 로 확인해야합니다.

```
client ip : 172.17.0.3
client port : 8002

server ip : 172.17.0.2
server port : 8001
```

실제 접속정보를 반영하여 코드를 아래와 같이 작성합니다.

아래 코드는 클라이언트에서 실행됩니다.

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8002))
server_socket.listen(1)

print("Listening ...")

client_socket, client_address = server_socket.accept()
print("Connection Accepted!")

data = client_socket.recv(1024)

print(f"Received data: {data.decode('utf-8')}")
client_socket.close()
```

이 코드를 실행합니다.

```python
python3 recv.py
```

 이제 nc 로 연결합니다.

```python
nc 172.17.0.3 8002
```

아래와 같이 listen 하고 있다가, 연결이 수립되면 문자열을 입력할 수 있게 됩니다.

서버에서 문자열을 입력하고 엔터로 전송하면 listen 쪽에서 출됩니다.

![Untitled](Untitled%20234.png)

![Untitled](Untitled%20235.png)

## 0.0.0.0

특이한 점은, 분명 받는 쪽에서는 주소를 입력할 필요가 없다고 배웠는데,

```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8002))
server_socket.listen(1)

print("Listening ...")
```

저기 보면 bind 에 연결 주소가 들어가는데다가 0.0.0.0 이라는 이상한 주소가 들어 있습니다.

이것은 “연결을 허용할 주소” 를 의미하는 란입니다. 저기에 특정 주소를 넣으면 해당 주소만 연결할 수 있고 다른 주소가 연결하면 거부됩니다. 콤마(,)로 구분하여 여러개의 IP주소들을 허용할 수도 있습니다.

그러나 우리는 모든 IP가 연결할 수 있도록 설정하고 싶을때가 있습니다. 예를 들어, 내가 홈페이지를 만들어서 인터넷에 공개하는 경우, 차단된 IP 일부를 제외하면 모두 연결가능해야합니다.

그렇다고 전세계 컴퓨터의 IP 주소를 알 수 없으니, “연결을 허용할 주소” 를 적을 수 없습니다.

따라서 IP주소에는 0.0.0.0 이라는 특별한 IP 주소가 있는데, 이건 모든 아이피주소를 의미하는 아이피주소입니다.

이것은 실제로 존재하는 IP주소는 아니므로, 0.0.0.0 으로는 아무것도 보낼 수 없습니다.

만일 nc -l 로 listen 하는 경우, 받는 주소가 자동으로 0.0.0.0 으로 설정되어 실행됩니다.

# Python Socket 으로 전송하고 Python Socket 로 받기

코드가 위에 있으니, 받는 쪽과 보내는 쪽의 Python code 를 각각 실행하여 연결이 되는 것을 확인해보세요.

성공한 결과는 아래와 같습니다.

![Untitled](Untitled%20236.png)

이것을 반복해서 해보면서, 소켓 프로그래밍을 통해 네트워크에 프로그램을 연결시키고, 다양한 응용을 해보기 바랍니다.

**현실의 모든 인터넷을 사용하는 프로그램은, 안에 소켓 프로그램이 코딩 되어 있습니다.**

계속