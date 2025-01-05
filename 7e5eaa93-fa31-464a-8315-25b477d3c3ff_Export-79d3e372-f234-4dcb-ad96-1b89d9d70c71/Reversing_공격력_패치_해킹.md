# Reversing : 공격력 패치, 해킹

<aside>
💡 author : agamtt(전재호) 2024-01-26
contributer : Firebear518(박현준) 2024-04-07

</aside>

# 패치, 크랙 (Patch, Crack)

이렇게, 게임이나 프로그램의 변수를 변경하여 새로 저장하는 것을 **패치(Patch)** 라고 부릅니다.

우리가 흔히 알고 있는 **크랙버전**은, 바이너리를 수정해서 정품버전이 아닌 프로그램을 유료버전인 것 처럼 속이는 패치를 한 것 입니다. 

이런걸 말합니다.

![Untitled](Untitled%20339.png)

우리는 grapple_story_2 를 패치해서, 드래곤을 쓰러뜨릴 수 있도록 만든 크랙버전을 만들 것 입니다.

# gdb 를 이용해서 패치할 부분 알아내기

<aside>
💡 **해킹 계획**

플레이어의 공격력을 설정하는 부분에서, 공격력값을 수정해서, 플레이어가 드래곤을 죽일 수 있을 만큼 강하게 바꿀 계획입니다.

</aside>

패치할 부분은 main+34 에서 플레이어의 공격력 6 을 스택 메모리에 복사하는 부분입니다.

![Untitled](Untitled%20340.png)

gdb 의 x 명령어를 사용하면 해당 부분의 기계어를 hex 로 출력할 수 있습니다.

형식은 아래와 같습니다.

```python
gdb> x/출력할길이 {메모리주소}
```

따라서 아래와 같이 입력합니다. 30은 적당히 크면 됩니다.

```python
gdb> x/30 *main+34
```

그러면 아래처럼 출력됩니다.

![Untitled](Untitled%20341.png)

우리가 바꿀 값은 6 이니, 0x06 이라는 값이 있을 겁니다.

아래에 있네요.

![Untitled](Untitled%20342.png)

# 출력 값이 16진수가 아닐 경우

아래처럼 16진수가 아니라 이상한 값이 출력되는 경우가 있습니다.

![Untitled](Untitled%20343.png)

이 경우엔 아래와 같이 입력해 출력 형태를 지정해주면 해결됩니다.

```python
gdb> x/30bx *main+34
(b: 1 byte 크기로 출력)
(x: 16진수 형태로 출력)
```

출력 결과는 아래와 같습니다.

![Untitled](Untitled%20344.png)

# 헥스 에디터를 이용해서 편집

이제 gdb 로 찾은 부분을 헥스 에디터로 찾아서 강제로 바꾸면 됩니다.

리눅스용 hex editor 인 hexedit 을 설치합니다.

```bash
apt install -y hexedit
```

hexedit 으로 실행파일 바이너리를 엽니다.

```bash
hexedit grapple_story_2
```

그러면 터미널창에서 hex editor 가 열립니다.

![Untitled](Untitled%20345.png)

이 프로그램의 메뉴얼은 아래 사이트에 나와있습니다.

[hexedit(1) - Linux man page](https://linux.die.net/man/1/hexedit)

Ctrl + S 를 누르면, 문자를 찾을 수 있습니다.

![Untitled](Untitled%20346.png)

우리가 찾을 부분은 이 부분입니다.

```
c7 45 f0 06 00 00 00 c7 45 ec ...
# 띄어쓰기를 없애면,
c745f006000000c745ec
```

이것을 Ctrl + S 를 누르고 입력하여 search 합니다.

![Untitled](Untitled%20347.png)

엔터를 치면 해당 부분으로 커서가 이동합니다. 

![Untitled](Untitled%20348.png)

우리가 원하는 부분을 찾았으니, 06 을 더 큰 값으로 수정합니다.

예를 들어, 0x6D 는 십진수로 109 이니, 체력 200인 드래곤을 두번만에 죽일 수 있습니다.

![Untitled](Untitled%20349.png)

![Untitled](Untitled%20350.png)

수정하고자 하는 값에 커서를 위치시키고,
Control + L 을 통해 해당 값을 수정합니다.

![Untitled](Untitled%20351.png)

수정한 후 저장합니다.

Ctrl + X 를 누르고, y 를 누르면 저장됩니다.

![Untitled](Untitled%20352.png)

이제 실행해보면,

![Untitled](Untitled%20353.png)

플레이어의 공격력 값이 0x6D, 즉 109 로 변조 되었습니다.

플레이어는 이제 짱 쎄졌기 때문에, 드래곤은 두 방이면 정리됩니다.

![Untitled](Untitled%20354.png)

축하합니다. 크랙버전으로 게임을 클리어했습니다.

![Untitled](Untitled%20355.png)

계속