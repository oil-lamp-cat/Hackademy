# Terminal 에서 github 로그인

<aside>
🏕️ 2024-03-13 전재호(agmtt)

</aside>

<aside>
💡 git push 등, repo의 code를 변경할 때는, 해당 repo 의 주인이거나 편집 권한을 가진 계정으로 로그인한 상태여야 한다.

</aside>

# Personal Access Token

github 는 **personal access token** 이라는 것을 지원하는데, 일종의 임시 비밀번호이다.

github 홈페이지에서 token을 생성한 후, 터미널에서 git push를 했을때 뜨는 id 에는 그냥 github id를 입력하고 비밀번호에 github 비밀번호 대신 이 token을 복붙하면 로그인이 된다.

token을 사용하려면 github 홈페이지에서 token을 생성해야한다. 그 방법은 다음과 같다.

github 홈페이지에서 Setting 을 들어간다.

![Untitled](Untitled%20253.png)

맨밑에 보면 developer Setting이 있다. 들어간다.

![Untitled](Untitled%20254.png)

Personal acess tokens 를 들어간다.

![Untitled](Untitled%20255.png)

![Untitled](Untitled%20256.png)

Generate new token 을 눌러서, 새 토큰을 만든다.

![Untitled](Untitled%20257.png)

Generate new token(classic) 을 누른다.

![Untitled](Untitled%20258.png)

Use your password를 사용하건 Mobile 인증을 하건 해서 들어간다.

![Untitled](Untitled%20259.png)

토큰 이름을 쓰고, Expiration을 설정한다.

Expiration에 기간을 설정하면, 그 기간이 지나면 토큰이 없어져서 그 토큰으로 로그인할수없다.

일종의 보안 기능이다.

귀찮으면 그냥 No expiration으로 설정한다.

repo 를 전부 체크해야 push를 할수있다.

맨 밑으로 내려서 Generate를 누른다.

![Untitled](Untitled%20260.png)

Make sure to copy your personal access token now. You won’t be able to see it again! 이라고 써있는게 보일것이다.

그렇다. token은 생성할때 한번만 보이고, 그다음엔 확인할수가없다. 만약에 까먹으면 토큰을 지우고 새로만들어야한다. 일종의 해킹방지 기능이다.

저걸 복사해서, 안전한 곳에 보관한 후, 로그인할때마다 입력해야한다.

### token 방식의 단점

password를 기억할수없다. 즉, push할때마다 token을 입력해야한다. (매우 귀찮다) 토큰을 credential 기능을 써서 pc에 저장하면 굳이 할수있긴한데… 그러면 해킹방지를 위해 token을 쓰는게 의미가 없다. 그 방법을 쓰면 로컬에 plain text로 저장되기 때문이다.