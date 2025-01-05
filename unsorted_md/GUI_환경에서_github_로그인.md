# GUI 환경에서 github 로그인

<aside>
🏕️ 2024-03-13 전재호(agmtt)

</aside>

<aside>
💡 git push 등, repo의 code를 변경할 때는, 해당 repo 의 주인이거나 편집 권한을 가진 계정으로 로그인한 상태여야 한다.

</aside>

# 첫번째 방법 : WEB 에서 로그인하기

![Untitled](Untitled%20249.png)

GUI 환경에서 git을 설치한 경우, **github credential manager** 라는 프로그램이 설치된다.

github 인증이 안된 컴퓨터에서 git push를 하려고 하면, 해당 창이 뜨는데, Sign in with your browser 를 누르면 브라우저를 열어서 github에 로그인 한 후, 리다이렉트 해서 인증된다.

또는 Sign in with a code 를 쓰면 핸드폰이나 이메일로 code를 보내준다.

*주의 : 웹브라우저가 있어야 하므로, **gui가 없는 리눅스나 ssh터미널에서는 사용이 불가능하다.**