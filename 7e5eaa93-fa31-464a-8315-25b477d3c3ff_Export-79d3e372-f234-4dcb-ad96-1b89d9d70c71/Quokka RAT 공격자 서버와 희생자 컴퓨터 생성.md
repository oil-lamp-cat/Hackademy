# Quokka RAT : 공격자 서버와 희생자 컴퓨터 생성

<aside>
⚠️ author : 전재호(agamtt) 2024-03-15
contributor : 손기민(KiminSon) 2024-04-07

</aside>

실습에 앞서, 공격자(해커) 역할을 할 서버 컴퓨터와, 희생자 역할을 할 컴퓨터를 도커로 생성합니다.

## 희생자의 컴퓨터 생성

해킹을 당하게 될 컴퓨터를 도커 컨테이너로 생성합니다.

(돈이 많은 사람은 컴퓨터를 직접 사도 됩니다.)

![Untitled](Untitled%20574.png)

이 kind_kalam 이라는 이름의 컨테이너가 오늘의 해킹 피해자입니다. (이름을 설정하지 않으면 도커 컨테이너는 랜덤이름으로 생성됩니다.)

<aside>
💡 **참고**

만일 도커 컨테이너에 이름을 짓고 싶다면 아래와 같은 명령어를 입력하고, 이름을 원하는 이름으로 하면 됩니다.

```bash
docker run -dit --name 이름 ubuntu
```

</aside>

![Untitled](Untitled%20575.png)

## 공격자의 C2 서버 생성

공격자가 희생자의 컴퓨터를 원격 조종하려면, C2 서버 (Command and Control) 가 필요합니다.

C2 서버는 희생자의 컴퓨터 안에 심어진 바이러스인 RAT 에 명령을 보내고(Command) 조종(Control) 합니다. C가 두개여서 C2 또는 C&C 서버라고 부릅니다.

공격자는 희생자의 RAT 으로 부터 연결 요청을 받아야하므로 포트를 열어 놓습니다.

아무포트나 사용하지 않는 포트를 두개 입력하여 포트포워딩하면 됩니다.

![Untitled](Untitled%20576.png)

생성된 quirky_booth 컨테이너가 오늘의 해커 역할을 할 컨테이너입니다.

<aside>
💡 **참고 : 실제로는 서로 다른 두개의 컴퓨터입니다.**
하나의 컴퓨터로 해킹 상황을 가정해보기 위해서 도커 컨테이너를 사용했습니다.

</aside>

![Untitled](Untitled%20577.png)

각각의 컨테이너를 Attach Visual Studio Code 로 열어서 창을 두개 띄워줍니다.

![Untitled](Untitled%20578.png)

그리고 두개의 창을 열어줍니다. 

<aside>
💡 다시 말하지만, 하나의 컴퓨터 안에서 실행되지만, 실제 해킹 상황에서는 두개의 서로 다른 컴퓨터 입니다!

</aside>

이때, 공격자의 컴퓨터와 희생자의 컴퓨터를 햇갈리지 않게 조심하세요.

아래 사진의 경우, 포트가 열려있는 quirky_booth 가 해커의 컴퓨터입니다.

![Untitled](Untitled%20579.png)

![Untitled](Untitled%20580.png)

이제 공격자와 희생자의 구분을 위해서 각각의 컨테이너에 접속한 후, 계정을 만들어줍니다.

희생자 역할을 할, 포트가 열려있지 않은 컨테이너에는 john 이라는 이름의 계정을 추가합니다.

sudo 권한도 주고, python도 설치합니다.

```bash
apt update
apt install -y sudo python3
adduser john
# 유저 생성 후,
usermod -aG sudo john
su john
```

공격자 역할을 할, 포트가 열려있지 않은 컨테이너에는 hacker 라는 이름의 계정을 추가합니다.

```bash
apt update
apt install -y sudo python3
adduser hacker
# 유저 생성 후,
usermod -aG sudo hacker
su hacker
```

이러면 준비는 끝입니다.

이제 hacker 는 john 의 컴퓨터에 악성코드를 심어서 컴퓨터의 제어를 뺏고자 합니다.

![Untitled](Untitled%20581.png)

john 의 컴퓨터가 해킹되었는지 알 수 있게 하기 위해, john 의 컴퓨터의 원하는 위치에 secret_password.txt 라는 파일을 만들어 줍니다.

추가)
그동안 root에서 실습해서 별다른 막힘이 없었나요?

어??? root에서 john, hacker로 넘어간 순간 뭐가 안된다구요?
ls 명령어가 말을 듣지 않나요?
secret_password.txt가 만들어지지 않나요?

그렇다면 Computer-Basic 과정에서 sudo 교안을 다시 읽고 오길 바랍니다.
(일단 모르겠으면 그냥 명령어를 칠때마다 앞에 sudo 붙이면 됨)

![Untitled](Untitled%20582.png)

계속