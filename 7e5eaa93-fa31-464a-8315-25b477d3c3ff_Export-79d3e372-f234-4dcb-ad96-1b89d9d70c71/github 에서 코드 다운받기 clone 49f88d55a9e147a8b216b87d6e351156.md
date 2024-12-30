# github 에서 코드 다운받기 : clone

<aside>
🏕️ 2024-03-13 전재호(agmtt)

</aside>

# clone

git 에서는 코드를 다운로드 받는 것을 download 가 아니라 clone 이라고 부른다.

# git 이 설치되어있는지 확인

git 이 컴퓨터에 설치되어있으면, 터미널에 git 이라는 명령어를 입력했을때 아래와 같이 떠야한다.

아래와 같이 출력되면 git 이 사용가능한 상태이다.

![Untitled](Untitled%20261.png)

# repo URL

레포지토리의 주소를 repo URL 이라고 한다.

이 repo URL 로 코드를 업로드하고 다운로드한다.

github 레포지토리에 접속하면 해당 레포의 repo URL 을 알 수 있다.

![Untitled](Untitled%20262.png)

![Untitled](Untitled%20263.png)

# clone 하고 싶은 폴더에서 터미널 열기

### Windows 에서 현재 폴더에서 cmd 열기

우클릭 후 “터미널에서 열기” 를 클릭하거나,

![Untitled](Untitled%20264.png)

원하는 폴더에서 파일 탐색기 주소창에 cmd 를 입력하면 됨

![Untitled](Untitled%20265.png)

### MacOS 에서 현재 폴더에서 터미널 열기

![Untitled](Untitled%20266.png)

# git clone

다운로드를 원하는 폴더에서 터미널을 연 상태에서 아래 명령어를 입력한다.

repository_url 은 github 의 레포에서 복사 붙여넣기한다.

```bash
git clone [repository_url]

## 예시
git clone https://github.com/agamtt/for_test.git
```

![Untitled](Untitled%20267.png)

아래와 같이 뜨면 clone 이 완료된 것 이다.

![Untitled](Untitled%20268.png)

<aside>
💡 **참고**
해당 폴더로 이동한다음, code 명령어로 vscode 에서 열면 편하다.
바로 해당 폴더가 vscode 에서 열린다.

![Untitled](Untitled%20269.png)

![Untitled](Untitled%20270.png)

</aside>

계속