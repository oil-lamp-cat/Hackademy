# 실습 : Visual Studio Code 에서 Docker 사용하기

<aside>
💡 author : 전재호(agamtt) 2024-03-15

</aside>

Visual Studio Code (vscode 라고 부르겠습니다.) 를 이용하면 파일 편집, 폴더 이동을 더 편리하게 할 수 있습니다.

vscode 를 실행하고, 네모 모서리가 떨어져나가는 아이콘(확장,Extension 아이콘입니다) 을 누르고, Docker 라는 확장팩을 설치합니다.

![Untitled](Untitled%2068.png)

이제 고래 아이콘을 누르면 도커 컨테이너들을 볼 수 있습니다.

![Untitled](Untitled%2069.png)

이제 각 기능에 대해 설명하겠습니다.

# Integrated Terminal (부착된 터미널)

cmd, Powershell Terminal 같은 터미널을 직접 열지 않고도 vscode 안에서 쓸 수 있습니다.

vscode 안에 포함된 터미널을 Integrated Terminal (인테그레이티드 터미널)이라고 부릅니다.

앞으로,  vscode 내장 터미널, 내장 터미널, integrated Terminal 등으로 부르면 모두 이것을 말하는 것으로 알아들으면 됩니다.

아래 단축키를 입력하면 integrated Terminal 을 열 수 있습니다.

```bash
Ctrl + `
```

또는, 맨 위 메뉴창에서 View 를 누르고 Terminal 을 누르면 열립니다.

![Untitled](Untitled%2070.png)

내가 어떤 운영체제에 설치했는지에 따라 종류가 바뀝니다.

저는 Windows 에 설치했으므로, Powershell 이 연결되어있습니다.

어떤 종류의 터미널이 부착되었는지는 여기에 표시됩니다.

![Untitled](Untitled%2071.png)

현재 vscode 가 어디에 연결되어있는지는 좌측 하단에 아이콘으로 표시됩니다.

만일 아래와 같이 >< 표시만 되어있다면, vscode 는 vscode 를 설치한 컴퓨터에 연결되어있습니다.

프로그램을 기준으로 그 프로그램이 설치된 본인의 컴퓨터를 **Local(로컬)** 이라고 부릅니다. 아래는 로컬에 vscode 가 연결되어있습니다.

![Untitled](Untitled%2072.png)

# 도커 컨테이너 생성을 vscode integrated terminal 에서 하기

앞서 말했다시피, vscode 의 integrated terminal 은 로컬의 터미널입니다. (내 컴퓨터의 터미널입니다.)

따라서 vscode integrated terminal 에서 도커 컨테이너를 생성할 수 있습니다.

도커 컨테이너를 생성하는 명령어를 vscode integrated terminal 에 입력해봅시다.

아래 명령어를 입력하면 됩니다.

```bash
docker run -dit ubuntu
```

도커 아이콘을 누르면 현재 컴퓨터에 설치된 도커 컨테이너들을 볼 수 있습니다.

![Untitled](Untitled%2073.png)

도커 컨테이너 생성 명령어를 입력하고 나면 이상한 문자열 (해시라고 부릅니다)이 뜨면서 컨테이너가 생성됩니다.

이제 좌측의 CONTAINERS 를 보면 컨테이너가 생성된 것을 볼 수 있습니다.

좌측하단을 보면 아직 vscode 의 integrated terminal 은 로컬, 즉 Windows 에 부착되어있습니다.

![Untitled](Untitled%2074.png)

이제 생성한 컨테이너에 마우스 우클릭을 누르고 Attach Visual Studio Code 를 누릅니다.

![Untitled](Untitled%2075.png)

그러면 새 창이 뜨는데, 이 vscode 는 도커 컨테이너에 integrated terminal 이 부착됩니다.

좌측 하단을 보면 확인할 수 있습니다.

![Untitled](Untitled%2076.png)

Ctrl + ` 또는 View/Terminal 을 클릭해서 마찬가지로 integrated Terminal 을 열 수 있습니다. 이 Termianl 은 리눅스 도커 컨테이너의 터미널인 것을 알 수 있습니다.

![Untitled](Untitled%2077.png)

# 파일 열기 (Open Folder)

A4 용지 두장이 겹쳐있는 것 같이 생긴 아이콘을 누르면 Open Folder 라는 버튼이 보입니다.

![Untitled](Untitled%2078.png)

Open Folder 를 클릭하고 / 를 입력한 후, Ok 를 누릅니다.

![Untitled](Untitled%2079.png)

그러면 좌측 메뉴창에서 도커 컨테이너에 있는 파일들을 확인할 수 있게 됩니다. 마우스 클릭으로 사용할 수 있어서, cd 와 ls 로 이동하는 것보다 편리합니다.

![Untitled](Untitled%2080.png)

# 유저 추가하고 파일 생성해보기

이제 유저를 추가하고 해당 유저로 전환한 후, 해당 유저의 home 폴더에 텍스트 파일을 만들어 보겠습니다.

terminal 에 아래 명령어를 입력합니다. name 은 자기 이름이나 닉네임 등 만들고 싶은 유저명을 입력합니다.

```bash
adduser name
```

명령어를 입력하면 New Password 를 입력하라고 합니다. 이것이 이 유저의 비밀번호 입니다.

- 비밀번호는 보안 상의 이유로 표시되지 않습니다.
- 엔터를 친 후, Retype new password 에 동일한 패스워드를 입력하면 됩니다. 패스워드가 불일치하면 유저가 생성되지 않습니다.
- 이제 유저정보를 입력받는데, 그냥 Enter를 입력해서 비워둬도 좋습니다. Enter를 여러번 누르면 유저가 생성됩니다.

![Untitled](Untitled%2081.png)

이제 생성한 유저로 로그인 합니다. name 은 아까 입력한 user 의 이름입니다.

```bash
su name
```

![Untitled](Untitled%2082.png)

이제 좌측 탐색기에서 /home/name 을 누르면 홈폴더의 파일들을 볼 수 있습니다.

![Untitled](Untitled%2083.png)

이제 아래 화면에 보이는 것처럼 A4용지 한장처럼 생긴 아이콘을 누르면 파일을 생성할 수 있습니다.

이름은 아무거나 적고 .txt 를 뒤에 붙여서 텍스트파일로 생성합니다.

그리고 아무거나 적습니다.

![Untitled](Untitled%2084.png)

이제 cd , ls , cat 으로 해당 파일을 터미널에서 확인해 볼 수 있습니다.

![Untitled](Untitled%2085.png)

계속