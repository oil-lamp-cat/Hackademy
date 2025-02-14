# 참고 : Apple Silicon MacOS (맥북, m 어쩌고 하는 칩) 에서 실습환경 구축(Qemu)

<aside>
⚠️

현재 맥북 Apple Silicon 의 Rosetta 는 ptrace 를 지원하지 않아서, 정상적인 방법으로는 gdb 정상 작동 불가능. 알려진 이슈임.
https://forums.docker.com/t/debugging-with-gdb-on-linux-amd64-docker-on-mac-m1-host/119321
https://forums.docker.com/t/emulation-for-x86-64-containers-on-aarch64-host/124533
https://forums.docker.com/t/cannot-run-amd64-images-on-my-m1-mbp/108691
https://forums.docker.com/t/docker-images-are-not-running-on-my-macbook-m2/138305

</aside>

# Apple Silicon MacOS : Qemu 를 이용한 Ubuntu 설치

## 1) 맥북 전원 켜기

![image.png](image%2065.png)

![image.png](image%2066.png)

![image.png](image%2067.png)

 여기까지 못하겠으면 맥북을 망치로 부순다음 깡통/캔 버리는 곳에 분리수거하시오.

## 2) Terminal 열기

**⌘ + space, Terminal 입력 후 엔터**

![image.png](image%2068.png)

 여기까지 못하겠으면 맥북을 망치로 부순다음 깡통/캔 버리는 곳에 분리수거하시오.

## brew 설치

**brew 가 이미 설치되어있으면 설치 안해도 됨.**

brew 설치 확인

```bash
brew --version
```

없으면 설치

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## qemu 설치

```bash
brew install qemu
```

 여기까지 못하겠으면 맥북을 망치로 부순다음 깡통/캔 버리는 곳에 분리수거하시오.

## ubuntu server 설치

```bash
cd Desktop && \
mkdir ubuntu2204 && \
cd ubuntu2204
```

ubuntu os 설치 이미지 다운로드

```bash
curl -o ubuntu2204.iso https://releases.ubuntu.com/22.04/ubuntu-22.04.5-live-server-amd64.iso
```

다운로드가 완료될 때까지 기다리기 (% 가 100 이여야 다 다운로드 된거임)

![image.png](image%2069.png)

아래 명령어를 입력해서, (bootable) 이라고 표시되는지 확인. 표시되지 않으면 잘못된 파일을 다운로드 받은 것임. (중간에 인터넷이 끊기거나, 링크를 잘못 입력한 것임. 명령어를 한번 더 확인하고 인터넷 연결 상태를 체크할 것)

```bash
file ubuntu2204.iso
```

![image.png](image%2070.png)

qemu 가상 드라이브(.qcow2) 파일을 생성. (기기에 20G 이상 용량이 남아있어야 함)

```bash
qemu-img create -f qcow2 ubuntu2204.qcow2 20G
```

![image.png](image%2071.png)

os bootable image (ubuntu2204.iso) 를 qemu 가상 드라이브(ubuntu2204.qcow2) 에 마운트

```bash
qemu-system-x86_64 -hda ubuntu2204.qcow2 -m 4096 -cdrom ubuntu2204.iso
```

![image.png](image%2072.png)

Try or Install Ubuntu Server 를 선택하고 엔터. 이후 기다리기

![image.png](image%2073.png)

기다리면 이 화면이 뜸. 다시 기다리기

![image.png](image%2074.png)

![image.png](image%2075.png)

English 선택 후 엔터

![image.png](image%2076.png)

Continue without updating 선택 후 엔터

![image.png](image%2077.png)

Done 선택 후 엔터

![image.png](image%2078.png)

방향키 위키로 Ubuntu Server (minimized) 선택 후, Done 선택 후 엔터

![image.png](image%2079.png)

Done 선택 후 엔터

![image.png](image%2080.png)

Done 선택 후 엔터

![image.png](image%2081.png)

Ubuntu archive mirror configuration 이 뜨면, 잠시 기다리기

![image.png](image%2082.png)

![image.png](image%2083.png)

![image.png](image%2084.png)

![image.png](image%2085.png)

Continue 선택 후 엔터

![image.png](image%2086.png)

Your name, Your Servers name, Pick a username, Choose a password, Confirm your password 입력. 이때, Pick a username 과 Choose a password 에 입력한 값은 기억하고 있어야함.

Pick a username : ubuntu / Choose a password, Confirm your password : ubuntu 로 입력

후 아래 방향키로 Done 선택 후 엔터

![image.png](image%2087.png)

Skip for now, Done 선택 후 엔터

![image.png](image%2088.png)

![image.png](image%2089.png)

방향키 아래로 계속 내려서 아무것도 선택 안하고 Done 선택 후 엔터

![image.png](image%2090.png)

기다리기

![image.png](image%2091.png)

Installation complete! 가 뜨면 성공

![image.png](image%2092.png)

이제 빨간색 버튼을 눌러서 Qemu 자체를 꺼줌.

![image.png](image%2093.png)

![image.png](image%2094.png)

이제 ubuntu2204.qcow2 에 os 가 설치됨.

아래 명령어로 os 부팅

```bash
qemu-system-x86_64 -hda ubuntu2204.qcow2 -m 4G
```

![image.png](image%2095.png)

엔터를 치면 login 프롬프트가 표시됨

![image.png](image%2096.png)

설치 시 설정한 username 과 password (ubuntu, ubuntu) 로 접속

![image.png](image%2097.png)

여기서 부터 진행하면 됨. 끝

이 os 에서 설치하거나 실행한 것은 ubuntu2204.qcow2 파일에 저장됨(약 20GB)

본인이 저장공간이 충분하고, qcow 를 백업해두고 싶다면 복사본을 생성해두는 것을 추천.

```bash
cp ubuntu2204.qcow2 ubuntu2204.qcow2.bkup
```

<aside>
💡

Qemu 의 기본 디스플레이에는 복사 붙여넣기가 안됨(다른 머신이여서, 메모리를 공유하지 않으므로 클립보드를 못쓰기 때문) 만일 클립보드를 사용하고 싶다면 ssh 연결 설정을 하고, 안하고 싶으면 아래는 안하고 패스해도 됨.

</aside>

### SSH 연결 설정

기존에 Qemu 가 켜져있다면 끄고, 아래 명령어로 포트 포워딩을 하여 다시 실행

```bash
qemu-system-x86_64 -m 4G -hda ubuntu2204.qcow2 -net user,hostfwd=tcp::8080-:22 -net nic
```

qemu 디스플레이가 열리면,

Host(=MacOS) 의 Terminal 에서 qemu 의 Ubuntu 로 접속하기 위해

qemu 의 shell 에서 아래를 수행

```bash
sudo apt update && sudo apt install -y openssh-server
```

부팅이 완전히 끝난 후, (아래와 같이 표시되어야함)

![image.png](image%2098.png)

MacOS 에서 Qemu 가 구동되고있는 Terminal 이외의 새로운 Terminal 을 열고, 아래를 실행

```bash
ssh -p 8080 ubuntu@localhost
```

그러면 연결 성공된다.

![image.png](image%2099.png)

이제 이 Terminal 을 통해 ssh 명령을 내려서 Qemu VM 을 제어할 수 있음. Terminal 을 통해 클립보트(복사, 붙여넣기)도 사용가능

![image.png](image%20100.png)

끝