# scp 로 파일 전송하기

<aside>
⚠️ author : 전재호(agamtt) 2024-03-15

</aside>

# SCP (Secure Copy)

scp 는 ssh 를 설치할 때 같이 설치되어 파일을 네트워크로 전송하는데 쓰입니다.

- ssh 는 명령어를 원격으로 전송합니다.
- scp 는 파일을 원격으로 전송하거나 다운로드 받습니다.

**scp 를 사용하려면 ssh 연결이 되어야 합니다.**

**scp 가 안되면 ssh 연결이 우선 되는지 점검해봐야합니다.**

# SSH 연결

리눅스에 ssh 접속을 위해서는 아래의 설정 및 설치가 필요합니다.

- apt 를 update 한다.
- apt 로 openssh-server, sudo 를 설치한다.
- adduser 로 유저를 추가한다.
- 그 유저를 sudo 그룹에 넣어서 sudo 명령어를 쓸 수 있게 한다.
- 텍스트 편집기로 sshd_config 에 AllowGroups sudo 를 추가해서 sudo 그룹이 ssh 접속할 수 있게 허용한다.
- sshd_config 를 바꿨으니, ssh 서버인 sshd 를 껐다 켜서 설정이 적용되게 한다.

이건 매번 하기 몹시 귀찮은 일이므로, 저번에 배웠던 쉘 스크립트로 만들어 놨습니다.

복붙해서 사용하면 편합니다.

```bash
## ssh_config.sh

echo "설정을 시작합니다..."

apt update

apt install -y openssh-server sudo vim net-tools

useradd -m -d "/home/$1" -s /bin/bash "$1"
cp -r /etc/skel/. "/home/$1"
echo "$1:$2" | chpasswd

usermod -aG sudo $1

if ! grep -q "^AllowGroups" /etc/ssh/sshd_config; then
    echo "AllowGroups sudo" | tee -a /etc/ssh/sshd_config > /dev/null
fi

if ! grep -q "^Port $3" /etc/ssh/sshd_config; then
    echo "Port $3" | tee -a /etc/ssh/sshd_config > /dev/null
fi

service ssh restart
```

apt 등을 포함하고 있으므로, root 권한으로 실행해야하며,

사용할 때는 argument 로 username, password, ssh_port 를 순서대로 입력합니다.

```bash
## 예시
./ssh_config.sh jeho 1234 8000
```

이때 포트는 포트포워딩에서 도커의 포트를 입력하여야 합니다.

```bash
호스트 포트:도커 포트
```

호스트 포트로 연결을 요청하면, 포트포워딩에 의해 도커 포트로 전달이 되고, 도커 포트에 연결된 ssh 가 응답합니다. 그러면 연결이 수립됩니다.

```bash
ssh 연결 요청 >> 호스트 포트:도커포트 >> openssh-server 응답
```

## ssh 연결 테스트

호스트 (도커를 설치한 컴퓨터, Windows 또는 MacOS) 에서 ssh 명령어를 이용해 도커 컨테이너 내부로 ssh 접속 테스트를 해보겠습니다.

호스트에서 아래 명령어를 수행해서 호스트포트 8003 과 도커포트 9999를 포트포워딩한 컨테이너를 생성합니다.

```bash
docker run -dit -p 8003:9999 ubuntu
```

![Untitled](Untitled%20224.png)

이 컨테이너는 호스트포트:컨테이너포트 가 8003:9999 로 포트포워딩된 상태입니다.

![Untitled](Untitled%20225.png)

이런 파일을 만들고 실행합니다.

```bash
## ssh_config.sh

echo "설정을 시작합니다..."

apt update

apt install -y openssh-server sudo vim net-tools

useradd -m -d "/home/$1" -s /bin/bash "$1"
cp -r /etc/skel/. "/home/$1"
echo "$1:$2" | chpasswd

usermod -aG sudo $1

if ! grep -q "^AllowGroups" /etc/ssh/sshd_config; then
    echo "AllowGroups sudo" | tee -a /etc/ssh/sshd_config > /dev/null
fi

if ! grep -q "^Port $3" /etc/ssh/sshd_config; then
    echo "Port $3" | tee -a /etc/ssh/sshd_config > /dev/null
fi

service ssh restart
```

이 파일을 실행합니다. 인자는 순서대로 username, password, port

```bash
./ssh_config.sh jeho 1234 9999
```

이제 도커 컨테이너에 ssh 연결을 요청합니다.

- 8003 포트는 호스트에 있습니다. 호스트 기준으로 호스트의 IP 는 localhost 입니다.
- ssh 연결 요청 >> 호스트 포트:도커포트 >> openssh-server 응답

```bash
ssh -p 8003 jeho@localhost
```

![Untitled](Untitled%20226.png)

호스트에서 도커 컨테이너로 연결이 잘 되었습니다.

# SCP 로 파일 다운로드하기

/remote/path/to/file : 도커 컨테이너에서 다운로드할 파일
/local/path/to/directory : 내 컴퓨터에 저장할 폴더
**주의 : scp 는 ssh 와 다르게 -P 가 대문자임.**

```bash
scp -P <port_number> user@remote_host:/remote/path/to/file /local/path/to/directory
```

폴더를 보내려면 -r 을 붙인다.

```bash
scp -r -P <port_number> user@remote_host:/remote/path/to/file /local/path/to/directory
```

# SCP 로 파일 업로드하기

/local/path/to/file : 내 컴퓨터에 있는 보낼 파일

/remote/path/to/directory : 도커 컨테이너에 저장할 경로

**주의 : scp 는 ssh 와 다르게 -P 가 대문자임.**

```bash
scp -P <port_number> /local/path/to/file user@remote_host:/remote/path/to/directory
```

폴더를 보내려면 -r 을 붙인다.

```bash
scp -r -P <port_number> /local/path/to/file user@remote_host:/remote/path/to/directory
```

# 실습해보기 : 컨테이너로 파일 보내기

file_to_send.txt 라는 파일을 만들고 아무거나 적는다.

![Untitled](Untitled%20227.png)

![Untitled](Untitled%20228.png)

이제 여기서 terminal 을 열고 scp 로 컨테이너로 보내봅시다.

![Untitled](Untitled%20229.png)

```bash
scp -P 8003 /C:\Users\girin\Desktop\file_to_send.txt jeho@localhost:/home/jeho/
```

![Untitled](Untitled%20230.png)

이제 컨테이너에 들어가서 확인해보면 파일이 전송 완료된 것을 확인할 수 있습니다.

![Untitled](Untitled%20231.png)

다운로드도 동일한 순서로 하면 됩니다.

계속