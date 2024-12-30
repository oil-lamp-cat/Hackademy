# gdb, pwndbg 설치, 실행, gdb CLI

<aside>
⚠️ author : 전재호(agamtt) 2024-03-15

</aside>

디버깅을 하기 위해, 디버거를 설치하겠습니다.

리눅스용 바이너리 디버거로는 gdb 가 가장 유명합니다.

다른 디버거의 사용법도 gdb 와 매우 유사하므로, gdb 를 배우면 다른 디버거도 쉽게 배울 수 있습니다.

# gdb 설치

gdb 는 gnu debugger 의 약자로, 리눅스용 디버거 입니다.

```bash
apt update && apt install -y gdb
```

# pwndbg 설치

pwndbg 는 gdb 용 플러그인입니다.

[GitHub - pwndbg/pwndbg: Exploit Development and Reverse Engineering with GDB Made Easy](https://github.com/pwndbg/pwndbg)

주의할 점은, root 권한으로 setup.sh 를 실행해서는 안됩니다. 그러면 root 만 pwndbg 를 사용할 수 있고, 일반 유저가 pwndbg 를 쓸 수 없습니다.

```bash
sudo apt install -y git

# git clone 할 디렉토리는 자유롭게 선택.
git clone https://github.com/pwndbg/pwndbg

# pwndbg 를 사용할 유저로 로그인한 상태에서 명령어를 수행. 
# sudo 는 root 유저로 명령어를 수행하므로, sudo ./setup.sh -> root 에 pwndbg 가 설치됨

cd pwndbg
./setup.sh
```

- git clone 을 하고 나면 pwndbg 라는 폴더에 pwndbg 설치파일을 내려 받습니다.
- pwndbg 폴더로 들어가서, setup.sh 를 실행하면 설치됩니다.

# gdb 와 pwndbg 가 잘 작동하는지 확인

이제 grappe_story 실행파일이 있는 디렉토리에서 아래의 명령을 수행합니다.

gdb 안에서 게임이 실행됩니다.

```bash
gdb ./grapple_story
```

이제, gdb 안에서 명령어를 내릴 수 있습니다.

이제 게임이 제대로 실행되는지 확인해봅시다. r 은 실행(run) 의 약자입니다.

```bash
pwndbg > r 
# 또는
pwndbg > run
```

게임을 종료하고 나가려면 quit 명령어를 입력합니다.

```bash
pwndbg > quit
```

# gdb CLI

아래는 리눅스의 쉘 입니다. 리눅스 쉘 커맨드를 실행합니다.

![Untitled](Untitled%20314.png)

gdb 를 실행하면 gdb 명령어를 실행할 수 있는 입력 란이 생깁니다.

명령으로 사람과 상호작용한다는 뜻에서, Command Linux Interface (CLI) 라고 부릅니다.

리눅스 쉘 명령어랑 햇갈리지 않도록 조심해야합니다.

gdb 명령어는 gdb CLI 에 입력해야합니다.

이것을 앞으로 **gdb CLI** 이라고 부르겠습니다.

![Untitled](Untitled%20315.png)

아래와 같이 쓰고 명령어를 쓰면, gdb 안에서 gdb cli 에 입력하라는 의미로 이해하면 됩니다.

<aside>
💡

pwndbg 가 설치되고 나면, gdb cli 의 입력창이 gdb> 에서 pwndbg> 로 바뀝니다

</aside>

```bash
pwndbg>
# 또는
gdb>
```

예시) gdb cli 에서 quit 입력하세요

```bash
gdb> quit
```

끝