# sudo 설치와 사용

<aside>
💡 author : agamtt 2024-03-15

</aside>

리눅스의 권한 관리는 복잡하지만, 보통 아래의 내용만 알면 됩니다.

그러니 이유는 나중에 설명하고, 실습을 통해 먼저 확인해보겠습니다.

docker container 를 처음 실행하면 root 로 로그인 됩니다.

![Untitled](Untitled%20138.png)

만일 su 명령어를 이용해 root에서 다른 유저로 switch user 했다면, exit 명령어를 실행하면 다시 이전 유저로 돌아올 수 있습니다.

adduser 로 유저를 만들고 확인해봅시다.

```bash
adduser username
```

(password 는 안 표시되는 것이 정상입니다.)

![Untitled](Untitled%20139.png)

유저가 전부 생성되고 나면 해당 유저로 su 해봅시다.

- su 는 switch user 의 약자로, 유저를 변경하는 명령어입니다.
- exit 은 su 로 변경했다가 다시 기존 유저로 돌아오는 명령어입니다.

![Untitled](Untitled%20140.png)

## sudo 설치 및 사용

sudo 는 root 가 아닌 계정으로, 한 줄의 명령어만 root 로 su 한 후 실행시키고, 다시 원래 계정으로 돌아오는 명령어입니다.

sudo 는 일반적으로 도커 컨테이너에 설치되어있지 않으므로, apt 로 설치해야합니다.

apt 는 프로그램을 설치하는 명령어로, sudo 를 설치하는 명령어는 아래와 같습니다.

프로그램 설치는 root 로 실행해야하므로, root 인 상태에서만 sudo 를 설치할 수 있습니다.

다른 유저로 로그인되어있다면 exit으로 root 로 변경한 후 설치합니다.

```bash
apt update
# 업데이트가 끝나면, 아래 명령어를 실행
apt install sudo
```

![Untitled](Untitled%20141.png)

![Untitled](Untitled%20142.png)

보통 apt install 하기 전에는 apt update 를 하므로, 두개의 명령어를 한줄로 실행하기 위한 명령어인 && 를 사용하여 둘을 연결합니다.

```bash
apt update && apt install sudo
```

이제 adduser 로 유저를 생성하고 sudo 를 사용해봅시다.

root 가 아닌 유저에게 sudo 를 사용할 수 있는 권한을 부여하려면 아래와 같이 입력합니다.

당연히 root 인 상태에서 부여해야합니다.

```bash
usermod -aG sudo username
```

![Untitled](Untitled%20143.png)

ls 명령어는 user 의 권한으로 실행되지만,

```bash
ls
```

sudo ls 는 root 의 권한으로 실행됩니다.

```bash
sudo ls
```

whoami 는 지금 누구로 로그인 되어있는지 출력하는 명령어입니다.

sudo 를 붙이면, root 라고 표시됩니다.

아래의 이유에서 입니다.

<aside>
💡 sudo 는 root 가 아닌 계정으로, 한 줄의 명령어만 root 로 su 한 후 실행시키고, 다시 원래 계정으로 돌아오는 명령어입니다.

</aside>

![Untitled](Untitled%20144.png)

이제 왜 그런지 자세히 설명해보겠습니다.

계속