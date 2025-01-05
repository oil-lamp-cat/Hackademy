# 고양이 홈페이지를 만들자 : php 환경세팅

<aside>
💡

author : 전재호(agamtt) 2023-12-05

</aside>

# 고양이 홈페이지

고양이가 나오는 홈페이지를 만들어보면서 웹 개발과 웹 해킹의 기본에 대해서 배워봅시다.

php 는 스크립트 언어인데 웹서버를 구동할 수 있습니다. ( 웹서버 : html 등을 내놓으라고 하면 주는 프로그램)

완성본은 아래와 같습니다.

![Untitled](Untitled%20382.png)

php 는 문법이 몹시 쉬워서 (파이썬이랑 동급) 파이썬을 할 줄 알면 순식간에 배울 수 있습니다.

2023년 기준 php 같은 구닥다리로 웹개발 안하고 django 나 spring 씁니다.

하지만 django 와 spring 을 먼저 하는 것은 몹시 어렵습니다.

php 로 개념을 먼저 배우면 두개를 나중에 배울 때 훨씬 빨리 배울 수 있습니다.

## 도커 컨테이너 만들기

```bash
sudo docker run -dit --name php_cat_homepage -p 8000:8000 ubuntu:22.04
```

이제 도커 컨테이너에 접속하여 필요한 패키지를 설치합니다.

## php 설치

```bash
sudo apt update
sudo apt install php
```

php 가 정상적으로 설치되었는지 확인합니다.

```bash
php -v
```

<aside>
💡

</aside>

php 파일을 만든 후, php 서버를 작동시키고, 웹브라우저로 접속해서 확인해보겠습니다.

아래와 같은 파일을 만들어서 php 가 정상적으로 작동하는지 확인합니다.

index.php 라는 파일을 만들고, 아래와 같이 적습니다.

```php
<?php
phpinfo()
?>
```

### php 서버 켜기

pwd 에 index.php 파일이 있는 상태에서 서버를 실행해야 합니다.

```bash
ls
# index.php 가 표시되어야함.
```

index.php 파일이 확인되면, 아래 명령어를 실행합니다.

S 는 Server 의 약자로, php 서버를 실행합니다.

0.0.0.0 이므로 어디에서나 접속할 수 있고, 도커의 8000을 호스트의 8000과 포워딩해두었으니 호스트의 웹브라우저로 도커 내부의 php 서버에 접속할 수 있습니다.

```php
php -S 0.0.0.0:8000
```

아래처럼 표시되면 잘 작동하는 것 입니다.

![Untitled](Untitled%20383.png)

### php 서버 끄기

아래 단축키를 입력하여 종료합니다.

```bash
Ctrl + C
```

## 참고 : 작동 원리

<aside>
💡

Windows, MacOS, Windows NT Server 등에서는 다를 수 있습니다만 기본 원리는 비슷합니다

</aside>

Linux 에 php 를 설치하면 (apt install php)

php 의 실행파일 (ELF 바이너리) 가 /usr/bin/ 에 있습니다.

실제로 이 디렉토리로 이동한 후, 경로를 명시하여 실행해도 작동합니다

```bash
cd /usr/bin
./php -v
```

php -S 는 php 자체 서버를 실행하는 옵션으로, 개발할 때 테스트용으로 보통 사용됩니다.

## 왜 php 같은 오래된걸 배우나요?

python, java 등의 웹 프레임워크를 이용하여 개발하면 (Django, Spring 등)

이미 많은 보안 관련 코드가 이미 코딩되어있습니다

아무것도 없는 상태에서 보안기능을 만들어보는 것이 원리를 이해하는데에 더 도움이 됩니다

어차피 원리는 똑같아서 뭘 배우건 상관이 별로 없음