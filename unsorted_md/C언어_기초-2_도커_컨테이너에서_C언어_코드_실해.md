# C언어 기초-2 : 도커 컨테이너에서 C언어 코드 실행하기

<aside>
💡 author : 전재호(agamtt) 2023-11-27

</aside>

## 도커 컨테이너 생성

C언어 코드를 실행하기 위해서는 도커 컨테이너로 작동하는 리눅스가 필요합니다.

도커 데스크톱으로 이미지를 검색합니다.

![Untitled](Untitled%20107.png)

ubuntu/nginx 를 검색합니다.

![Untitled](Untitled%20108.png)

![Untitled](Untitled%20109.png)

실행하면 컨테이너가 실행됩니다.

이름을 설정하지 않았으므로, 도커가 랜덤 이름을 붙입니다. (꽤 재밌습니다.)

![Untitled](Untitled%20110.png)

Containers 탭을 클릭하면 현재 컴퓨터에 설치된 가상 컴퓨터인 Container 의 목록을 볼 수 있습니다.

![Untitled](Untitled%20111.png)

<aside>
🔥 3번 생성했더니 재밌는 이름이 많이 생겼습니다.
musing_beaver (숙고하는 비버)
peaceful_meitner (평화로운 마이트너 (스웨덴의 물리학자 리제 마이트너))
sharp_liskov (날카로운 liskov (프로그래머 리스코브)

</aside>

exec 탭에 들어가면, docker conainer 컴퓨터의 shell 에 직접 명령어를 입력할 수 있습니다

![Untitled](Untitled%20112.png)

ls 를 입력해보면, 명령어가 잘 실행됩니다.

![Untitled](Untitled%20113.png)

이제 필요한 툴을 설치해줍니다.

일단 화면이 이것저것 출력되어있어서 지저분하니, 화면을 지웁니다.

```bash
clear
```

apt 를 업데이트합니다. apt 는 리눅스의 앱스토어나 플레이스토어 같은 것인데, apt 가 설치할 수 있는 패키지 (리눅스에서 프로그램) 목록을 가져옵니다.

```bash
apt update
```

![Untitled](Untitled%20114.png)

apt 가 업데이트되었으면, nano 부터 설치합니다. nano 는 리눅스용 텍스트 에디터로, 리눅스의 메모장 같은 것 입니다. 이걸로 코딩을 할 것 입니다.

```bash
apt install nano
```

gcc 도 설치해줍니다.

gcc 는 gnu 라는 팀에서 만든 C compiler 입니다. C언어 소스코드를 실행파일로 바꾸는 “컴파일”을 하는 프로그램입니다.

```bash
apt install gcc
```

![Untitled](Untitled%20115.png)

중간에 Do you want to continue? [Y/n] (너 진짜 설치할거냐?) 라고 물어보는데, y 를 입력하고 엔터를 칩니다. 그러면 설치됩니다.

이제 nano 로 C언어 소스코드를 짜보겠습니다.

우선, home directory 로 이동합니다. 이상한 폴더에다가 작성하면 안되니까요

cd ~ 는 홈디렉토리로 이동하는 간단한 명령어입니다.

```bash
cd ~
```

이제 nano 로 소스코드 파일을 생성합니다.

이름은 myprogram.c 로 합시다. (뭘로해도 상관없음)

```bash
nano myprogram.c
```

![Untitled](Untitled%20116.png)

![Untitled](Untitled%20117.png)

그러면 이제 텍스트 에디터가 myprogram.c 를 생성한다음 편집할 수 있게 해줍니다.

이제 이렇게 C 코드를 짜줍니다.

```bash
#include <stdio.h>

int main(){
puts("hello im superhacker");
return 0;
}
```

![Untitled](Untitled%20118.png)

아래를 잘보면, ^O Write Out 이라고 써있습니다.

^O 는 키보드 Ctrl 를 누른 상태에서 키보드 O 를 누르라는 뜻입니다. 

Write Out (써버리다) 는 Save 와 똑같은 말입니다. 파일을 저장하는거죠. (왜 단어를 통일하지 않는걸까요?)

^O 로 저장을 해줍니다.

아래에 File Name to Write : 가 뜨면, 엔터를 칩니다.

그럼 저장됩니다.

![Untitled](Untitled%20119.png)

![Untitled](Untitled%20120.png)

이제 nano 를 끄고, myprogram.c 가 잘 생성되었는지 확인해봅시다.

아래를 보면 알 수 있듯이, 나가기는 ^X 입니다. (Ctrl + X)

ls 와 cat 으로 확인해보면, 파일이 잘 생성되었고 안에는 우리가 짠 C 코드가 들어있습니다. 성공~

![Untitled](Untitled%20121.png)

## 컴파일

이제 gcc 를 이용해서 컴파일해서 실행해봅시다.

(사실 gcc 를 안써도 되고 다른 c 컴파일러를 써도 되는데 gcc 가 제일 유명합니다.)

gcc 로 myprogram.c 를 컴파일하려면 반드시 ls 를 했을때 현재폴더에 myprogram.c 가 있어야합니다. 여러 폴더에 myprogram.c 가 있을수도있는데, gcc가 그중에 어느것인지 어떻게 알겠어요? 

ls 를 해서 myprogram.c 가 있으면 gcc 로 컴파일합니다.

gcc 로 c 소스코드파일을 컴파일하려면 아래 명령어를 입력합니다.

```bash
gcc {{sourcecode.c}}
```

우리 소스코드의 이름은 myprogram.c 니까 이렇게 입력합시다.

```bash
gcc myprogram.c
```

그리고 나서 ls 를 하면, a.out 라는 파일이 생겨있습니다. gcc 가 컴파일해서 생성한 것 입니다.

a.out 은 myprogram.c 가 이러쿵저러쿵 컴파일이 되어서 나온 실행파일입니다.

<aside>
🔥 참고로 이러쿵저러쿵 컴파일 과정은 보통 알빠아니므로 몰라도 됩니다.
자세한걸 배우려면 컴퓨터공학과 전공과목인 “컴파일러” 나 “프로그래밍언어론” 을 공부해보세요.

</aside>

![Untitled](Untitled%20122.png)

이제 a.out 을 실행해봅니다.

전에도 배웠듯, 그냥 a.out 을 입력하면 리눅스는 명령어라고 생각해서 /bin 에서 찾습니다. 당연히 없으므로 실행에 실패합니다.

![Untitled](Untitled%20123.png)

경로를 포함해서 실행해야합니다. 전체경로를 쓰거나, dot notation (리눅스쉘에서 점은 현재경로로 바뀌어서 실행됩니다) 를 쓰세요. 즉 아래와 같이 입력합니다.

```bash
/root/a.out
또는
./a.out
```

그러면 잘 실행되어서 hello im superhacker 가 화면에 출력됩니다.

![Untitled](Untitled%20124.png)

<aside>
🔥 **토막상식**
a.out 는 gcc 에서 이름을 지정하지 않고 컴파일했을때의 기본 이름입니다.
컴파일은 일종의 조립인데, 조립된(assemble) 코드라는 뜻에서 그렇게 붙었습니다.

</aside>

### 이름 지정

소스코드가 하나면, a.out 으로 생성하면 이름을 정할 필요가 없으니 편합니다.

그러나, 소스코드가 한 폴더에 여러개면,

a.out 으로 생성되면 당최 이게 어떤 코드에서 컴파일된건지 알수가 없습니다.

따라서 이름을 지정하여 컴파일하도록 합시다.

이름을 지정하여 컴파일하려면 이렇게 합니다.

```bash
gcc -o {{output_filename}} {{source_code}}
```

그런데, c 소스코드파일은 .c 가 붙어있으니, 보통 컴파일된 파일이름은 이름부분은 똑같게 하고, 확장자만 없애는 식으로 많이들 합니다.

즉, myprogram.c 를 컴파일해서 myprogram 라는 실행파일을 만듭니다.

```bash
gcc -o myprogram myprogram.c
```

그리고, 명령어 옵션은 위치에 무관하므로, 아래와 같이 해도 똑같이 실행됩니다.

```bash
gcc myprogram.c -o myprogram
```

![Untitled](Untitled%20125.png)

이제 어떤 C 소스코드가 있을때, 그것을 컴파일해서 실행하는 방법을 배웠습니다.

계속