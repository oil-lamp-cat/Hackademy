# docker container 에 root 권한으로 접속하기

<aside>
💡

author : agamtt 2023-11-30

</aside>

# 실습 환경 만들기

<aside>
💡 **여기를 참고합니다.**

[실습 : 컨테이너 두개 만들고 포트포워딩하기](%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%B3%E1%86%B8%20%E1%84%8F%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%82%E1%85%A5%20%E1%84%83%E1%85%AE%E1%84%80%E1%85%A2%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%A9%20%E1%84%91%E1%85%A9%E1%84%90%E1%85%B3%E1%84%91%E1%85%A9%E1%84%8B%E1%85%AF%E1%84%83%E1%85%B5%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20995d9cf49347438e9eaa9ecc47cac664.md)

</aside>

## ssh 로 루트 권한 사용하기

현재 guest1 은 sudo 권한이 없으므로 root를 사용할 수 없습니다.

![Untitled](Untitled%20222.png)

ssh 로 root 로 접속하면 안된다고 배웠습니다.

그러나 apt 설치 등을 하려면 root 계정이 필요합니다.

ssh 로 어떻게 root 를 사용할 수 있을까요?

그것은 일반유저를 sudo 그룹 포함시킨 후, sudo 그룹에 속한 계정들을 모두 접속 허용하면 됩니다.

그리고 root 권한명령은 su root 하지말고 sudo 를 사용하여 수행합니다.

우선 server 에 sudo 를 설치합니다. (guest1에서 말고 root에서 설치해야 함) 

```bash
apt update
apt install sudo
```

<aside>
⚠️ **참고: root 계정에서 일반 계정으로 이미 su 해버린 경우**
exit 명령어를 입력하면 다시 root 로 돌아옵니다.
exit : 바로 직전에 로그인한 사용자로 전환하는 명령어

</aside>

그리고 guest1 계정을 sudo 그룹에 추가합니다. (당연히 root 계정으로 해야함)

명령어는 아래와 같습니다.

```bash
usermod -aG sudo guest1
```

<aside>
💡 a 는 append 의 약자이고, G는 Group 의 약자입니다.
-는 리눅스의 옵션을 의미하는 접두자입니다.

</aside>

sudo 그룹을 확인해보면 guest1 이 sudo 에 속해있습니다.

```bash
cat /etc/group
```

![Untitled](Untitled%20223.png)

ssh 연결을 종료한 후, 재접속해보면 sudo 를 사용할 수 있습니다.

```bash
exit

ssh -p 9001 guest1@172.17.0.2

sudo echo "hello"
```

계속