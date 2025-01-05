# Visual Studio Code 와 Docker 연결

<aside>
💡 author : 전재호(agamtt) 2023-09-23

</aside>

# Visual Studio code 란

Visual Studio Code 는 2023년 가장 널리 쓰이는 코드 편집기입니다. 보통 vscode 라고 줄여서 부릅니다.

# Visual Studio Code 설치

우선 visual studio code 를 컴퓨터에 설치합니다.

[맥에서 VS Code 설치하는 방법](https://www.lainyzine.com/ko/article/how-to-install-visual-studio-code-on-macos/)

[[Windows] Visual Studio Code 설치](https://hbase.tistory.com/346)

그리고 vscode 에 docker 를 연동하기 위하여 docker extension을 설치합니다.

**<2. 필요한 기능 추가하기>**까지만 하면 됩니다.

**<3. VS code와 Docker 연동하기>**부터는 하지 않아도 됩니다.

[6-3. VS code에 Docker 연동하기! (with Jupyter notebook)](https://89douner.tistory.com/123)

이제 docker 아이콘 모양 탭을 클릭한 후, 우클릭/attach Visual Studio Code 버튼으로 열면 컨테이너에 접속됩니다.

![Untitled](Untitled%2022.png)

이제 ctrl ` 를 누르거나 View/Terminal 을 클릭하여 쉘을 엽니다.

![Untitled](Untitled%2023.png)

이제 다음을 입력하여 제대로 작동하는지 확인합니다.

```bash
cd /
ls
```

![Untitled](Untitled%2024.png)

위와 같이 출력되면 정상 작동하는 것 입니다.

계속