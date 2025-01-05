# Windows 와 MacOS 의 쉘, 터미널

<aside>
🏕️ 2024-03-13 전재호(agmtt)

</aside>

# Shell

거의 모든 운영체제는 쉘을 가지고 있습니다.

<aside>
💡 **참고
”**거의” 인 이유는 아이폰 등의 특수한 경우는 쉘을 막아놓았기 때문에…

</aside>

Windows 에도 Shell 이 있고, MacOS 에도 Shell 이 있습니다. 따라서 쉘커맨드로 작동시킬 수 있습니다.

또한, Shell 과 통신하는 프로그램을 기본 프로그램으로 설치해놓았습니다.

- Windows 의 터미널은 cmd, powershell 두개 중에 맘에 드는 것을 쓰면 됩니다.
- MacOS 의 터미널은 Terminal 이라는 앱입니다.
    - zsh, iterm 등을 설치해서 사용할 수도 있습니다.

# 실습

<aside>
💡 본인이 가지고 있는 노트북/컴퓨터가 Windows 인지 MacOS 인지 몰라서, 둘다 준비했습니다. 각자 운영체제에 맞게 따라해보면 됩니다.

</aside>

# Windows cmd

Windows 에서 cmd 커맨드를 사용해 보겠습니다.

[[PC] Window CMD 사용하기! 명령프롬프트 명령어 모음!](https://kecoz.tistory.com/92)

검색창에 cmd 를 검색하여 실행합니다.

![Untitled](Untitled%2061.png)

리눅스에서 ls 는 list 의 약자입니다.

Windows 에서는 명령어가 다릅니다. cmd 에서 ls 와 동일한, 디렉토리의 파일과 폴더 목록을 출력하는 명령어는 dir 입니다.

```bash
dir
```

![Untitled](Untitled%2062.png)

터미널 내용 지우기는 리눅스에서는 clear 이고, Windows 에서는 cls 입니다.

```bash
cls
```

# MacOS Terminal

맥에서 터미널을 사용해보겠습니다. 검색창에 “터미널” 또는 “Terminal”을 입력하거나 앱 목록에서 터미널을 찾아서 클릭합니다.

![Untitled](Untitled%2012.png)

그러면 맥의 쉘과 연결된 터미널이 열립니다.

![Untitled](Untitled%2063.png)

ls 를 입력해보면, 파일과 폴더 목록이 표시되는 것을 알 수 있습니다.

![Untitled](Untitled%2064.png)

[Mac용 터미널 사용 설명서](https://support.apple.com/ko-kr/guide/terminal/welcome/mac)

[[Mac] 맥 터미널 기본 사용법을 배워보자](https://mini-min-dev.tistory.com/102)

계속