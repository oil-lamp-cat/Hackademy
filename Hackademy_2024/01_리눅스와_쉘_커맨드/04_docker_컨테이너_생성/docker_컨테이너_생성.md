# docker container 에 ssh 접속하기

<aside>
💡 author : agamtt 2023-11-30

</aside>

# 실습 환경 만들기

<aside>
💡 **여기를 참고합니다.**

[실습 : 컨테이너 두개 만들고 포트포워딩하기](%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%B3%E1%86%B8%20%E1%84%8F%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%82%E1%85%A5%20%E1%84%83%E1%85%AE%E1%84%80%E1%85%A2%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%A9%20%E1%84%91%E1%85%A9%E1%84%90%E1%85%B3%E1%84%91%E1%85%A9%E1%84%8B%E1%85%AF%E1%84%83%E1%85%B5%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20995d9cf49347438e9eaa9ecc47cac664.md)

</aside>

ssh 란 secure shell 의 약자로, 인터넷을 통해 터미널을 사용할 수 있게 해줍니다.

세상에 있는 거의 모든 “서버” 는 ssh 를 통해 원격 접속되어 관리됩니다.

**개발자, 서버관리자, 해커 모두 ssh 를 사용합니다.**

![Untitled](Untitled%20212.png)

ssh 를 사용하면, 먼 곳에 있는 리눅스, Windows, MacOS 에 원격으로 접속하여 명령어를 실행할 수 있습니다.

![Untitled](Untitled%20213.png)

<aside>
💡 **참고**
안드로이드와 아이폰의 경우, 루팅과 탈옥을 하면 ssh 접속을 할 수 있게 되지만 굳이 그렇게 하지는 않습니다.
스마트냉장고나 스마트TV, 인터폰 등 에는 ssh 접속을 할 수 있습니다. (그렇게 해킹을 합니다.)

</aside>

# open ssh

open ssh 는 널리 쓰이는 ssh 프로그램입니다.

ssh 도 네트워크 통신으로 작동하므로, client 와 server 가 있어야합니다.

접속하려는 쪽은 ssh-client 가, 접속을 제공하는 서버쪽에는 ssh-server 가 설치되어있어야합니다.

## ssh client

client 에 ssh-client 를 설치합니다. ssh-client 의 이름은 ssh 입니다.

```bash
apt update
apt install ssh
```

ssh 를 입력하였을때 아래와 같이 출력되면 정상적으로 설치된 것입니다.

![Untitled](Untitled%20214.png)

## ssh server

ssh 는 기본적으로 22번 포트를 사용하기로 전세계가 약속을 했습니다.

(물론 포트번호를 바꿀 수도 있습니다.)

server 역할을 할 컴퓨터에 openssh-server 를 설치합니다.

```bash
apt update
apt install openssh-server 
```

중간에 설치하겠냐고 물어보면 y 를 치고 엔터, 그리고 중간에 어느나라에 살고있는지 물어보면 Seoul 을 선택하면 됩니다.

설치 완료 후,  아래 명령어를 통해 ssh-server 가 작동중인지 확인할 수 있습니다.

service 명령어는 root 권한을 필요로 합니다.

```bash
service ssh status
```

ssh-server를 켜고 끄는 명령어는 아래와 같습니다. (restart 는 stop 한 후 start 합니다.)

```bash
service ssh start
service ssh stop
service ssh restart
```

![Untitled](Untitled%20215.png)

기본적으로 ssh-server 를 설치하고나면 접속 불가능합니다. (당연합니다. 설치하자마자 누구나 들어올 수 있으면 안됩니다.)

이제 openssh-server 에 접속가능하도록 설정해야합니다.

## 접속 포트 변경

기본 포트는 22인데, 현재 8001 포트만 host 와 연결되어있습니다.

따라서 포트번호를 바꿔야합니다.

```bash
apt update
apt install nano
```

open-ssh 설정파일을 열어줍니다. /etc/ssh/sshd_config 에 있습니다.

```bash
nano /etc/ssh/sshd_config
```

#으로 되어있는 부분은 기본적으로 설정이 어떻게 되어있는지 나타냅니다.

해당 부분을 지우고 원하는 설정을 입력하면 됩니다.

![Untitled](Untitled%20216.png)

9001 포트를 사용할 것이므로 지우고 9001로 적어줍니다. #까지 지워야합니다.

![Untitled](Untitled%20217.png)

nano 에서는 Ctrl+O , Enter, Ctrl+X 를 입력하면 저장됩니다.

설정을 적용하려면 ssh-server 를 껐다켜야합니다.

```bash
service ssh restart
```

<aside>
💡 **참고**
참고로 ssh-server 에는 root 로 접속할 수 없도록 기본설정되어있고, 가능하도록 바꿔서도 안됩니다.

해킹사고의 일부는 ssh-server 에 root 로 접속하는 비밀번호가 유출되어서 일어납니다.

</aside>

따라서 ssh 접속용 계정을 만듭니다.

유저계정을 생성하고 비밀번호를 입력합니다.

```bash
adduser guest1
```

<aside>
👨🏻‍💻 **부연설명**
client라는 컴퓨터가, server라는 컴퓨터에, ”특정 유저”로 접속한다는 의미입니다.
그러니, server라는 컴퓨터에 guest0이라는 계정을 만드셔야합니다!
(client 컴퓨터가 아니라)

</aside>

## 접속 허용 계정으로 추가하기

그리고 다시 nano 로 설정파일을 열어서 해당 계정을 적어줍니다.

```bash
nano /etc/ssh/sshd_config
```

아래와 같이 추가해야합니다. 적는 위치는 몇번째줄인지 무관합니다.

```bash
AllowUsers {{username}}
```

꼭 AllowUser 가 아니라 AllowUsers 여야하고 username 은 실제 존재하는 계정명으로 바꿉니다.

![Untitled](Untitled%20218.png)

nano 에서는 Ctrl+O , Enter, Ctrl+X 를 입력하면 저장됩니다.

설정을 적용하려면 ssh-server 를 껐다켜야합니다.

```bash
service ssh restart
```

이제 net-tools 를 설치한 후 ip 를 확인합니다.

```bash
apt update
apt install net-tools
ifconfig
```

![Untitled](Untitled%20219.png)

접속하려면 아래와 같은 형식으로 입력합니다.

```bash
ssh -p {port} {user}@{ip}
```

실제 접속정보에 맞게 수정하면 아래와 같습니다.

```bash
ssh -p 9001 guest1@172.17.0.2
```

<aside>
💡 **연결 신뢰**
이 연결을 신뢰합니까? 하고 물어보면 yes 를 입력합니다.

![Untitled](Untitled%20220.png)

</aside>

아래와 같이 뜨면 성공입니다.

잘 보면, client 에는 guest1 이라는 유저를 생성한 적이 없는데 현재 guest1 으로 로그인이 되어있습니다.

해당 계정으로 원격접속이 된 것 입니다.

![Untitled](Untitled%20221.png)

다시 원래 터미널로 나가려면 exit 명령어를 입력합니다

```bash
exit
```

계속