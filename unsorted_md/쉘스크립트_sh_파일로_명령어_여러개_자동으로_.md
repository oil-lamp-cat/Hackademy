# 쉘스크립트 : sh 파일로 명령어 여러개 자동으로 실행하기

<aside>
⚠️ author : agamtt(전재호) 2024-03-15

</aside>

명령어 여러개를 매번 사람이 손으로 입력하는 것은 힘든 일입니다.

리눅스는 여러개의 명령어를 미리 파일로 저장해두고, 실행해서 명령어를 자동으로 한번에 실행하는 것을 지원합니다.

이러한 기능을 쉘 스크립트(Shell Script) 라고 부릅니다.

MacOS 에서는 동일하게 Shell Script 라고 부르고, Windows 에서는 배치 스크립트 (Batch) 배치파일이라고 부릅니다.

![Untitled](Untitled%20169.png)

![Untitled](Untitled%20170.png)

# 리눅스 쉘 스크립트 실습

쉘 스크립트를 직접 만들고 써봅시다.

쉘 스크립트파일은 .sh 로 끝납니다.

[test.sh](http://test.sh) 라는 파일을 만들고, 안에 이렇게 적습니다.

whoami 를 두번 실행하고, hello linux 를 출력합니다.

![Untitled](Untitled%20171.png)

쉘스크립트 파일을 실행하려면 해당 파일에 실행 권한이 있어야 합니다. (그렇지 않으면 아무 파일이나 실행시킬 수 있게 되어, 악성코드에 취약해지니까요)

*chmod 명령어를 사용하려면 root 이거나, sudo 를 사용해야합니다.

실행권한을 부여하는 명령어는 아래와 같습니다.

root 라면 sudo 를 붙이지 않아도 됩니다.

```bash
# x (execute의 약자) 권한을 부여
sudo chmod +x test.sh 
```

![Untitled](Untitled%20172.png)

이렇게 출력되면 성공입니다.

이러한 쉘 스크립트는 프로그램 설치나 유저 생성 등 귀찮은 일을 한번에 할 수 있게 해줍니다.

# 쉘스크립트에 인자(argument) 넣기

쉘스크립트에는 변수를 삽입할 수 있습니다. 쉘 스크립트를 실행할 때마다 다른 값을 넣어서 실행할 수 있다는 것이죠.

[test.sh](http://test.sh) 파일에 이렇게 적습니다.

```bash
echo "첫번째 argument : $1"
echo "두번째 argument : $2"

whoami

echo "실행 끝냅니다"
```

이제 실행시킬때, ./test.sh 뒤에 문자나 숫자를 입력하면 $1 과 $2 가 해당 값으로 바뀌어 실행됩니다.

![Untitled](Untitled%20173.png)

# 쉘 스크립트를 어따 쓰는가

쉘 스크립트를 이용하면 프로그램 여러개 설치같은 귀찮은 일을 한번에 자동으로 할 수 있습니다.

예를 들면 이런 쉘 스크립트를 실행하면 vim 과 python3 를 자동으로 설치한다음 프로그램 설치가 완료되었다는 메세지를 출력합니다.

```bash
echo "꼭 필요한 프로그램들을 설치합니다..."

apt install -y vim

apt install -y python3

echo "프로그램 설치가 완료되었습니다..."
```

```bash
sudo ./test.sh
```

![Untitled](Untitled%20174.png)

계속