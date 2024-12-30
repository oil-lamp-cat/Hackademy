# git config : commit 계정 정보 설정

<aside>
🏕️ 2024-03-13 전재호(agmtt)

</aside>

git에 이름없이 올리면 누가 올렸는지 모른다. 그래서 git 프로그램 안에는 push 할때 보내는, 보내는사람 정보를 설정해야 push 할수있다.

즉, commit 할때, 그안에 들어가는 계정 정보를 설정한다.

```bash
git config --list //현재 git init 의 commit에 담을 계정 조회
git config --list --global //git이 설치된 컴퓨터 전체(전역)의 commit에 담을 계정 조회

git config –-global user.name "USER_NAME"
git config –-global user.email "USER_EMAIL"
```

*근데 이건 github 의 계정 로그인 정보랑은 전혀 다른거다.

같지 않아도 되고, 아무런 관련이 없다.

## Windows 와 Linux 에서 git config 차이

git config —list 이렇게하면 계정정보가 안뜬다.

이유)

어째서인지 windows git에서는 그냥 git config 와 git config —global이 분리되어있다.

리눅스시스템에서는 git config —list >> global과 local이 모두 뜨지만 windows는 global이 안뜬다.

git config —global —list 

>> [user.email](http://user.email) = test1@gmail.com

>> [user.name](http://user.name) = John

git config  —global —unset user.email

git config —global [user.name](http://user.name) “john”

**문자열을 받고, 띄어쓰기로 구분, =이 없다는 점에 주의한다

끝.