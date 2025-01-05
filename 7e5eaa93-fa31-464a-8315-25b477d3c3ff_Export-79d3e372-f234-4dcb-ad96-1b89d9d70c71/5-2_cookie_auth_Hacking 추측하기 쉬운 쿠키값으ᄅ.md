# 5-2_cookie_auth_Hacking : 추측하기 쉬운 쿠키값으로 인한 취약점

<aside>
💡 author : 전재호(agamtt) 2024-01-24

</aside>

우리가 babo 유저인데, grape 의 개인페이지를 보고싶다고 가정해봅시다.

babo 는 해킹 동아리 회원이여서, Cookie Poisoning 공격기법을 알고 있습니다.

babo 는 우선, 자신의 회원정보인 아이디 babo, 비밀번호 babo1234 로 사이트에 로그인합니다.

 

![Untitled](Untitled%20446.png)

그러면 user:babo_cookie 라는 쿠키가 생성됩니다.

![Untitled](Untitled%20447.png)

# 추측1

해커 babo 는 여기서 의심을 해봅니다.

<aside>
💡 혹시 이 user 라는 cookie 로 사용자 인증을 처리하는게 아닐까?
user cookie 값을 바꾸면 어떻게 될까?

</aside>

이 가설을 테스트해봅니다.

user cookie 를 아무값으로나 변조합니다. (Cookie Poisoning)

그리고 새로고침 해봅니다.

![Untitled](Untitled%20448.png)

그러면 goback.php 로 리다이렉트되고, 잘못된 접근이라고 나옵니다.

![Untitled](Untitled%20449.png)

다시 user 쿠키를 babo_cookie 로 바꾼 뒤 babo-page.php 에 접속합니다.

![Untitled](Untitled%20450.png)

![Untitled](Untitled%20451.png)

가설이 맞는 것 같습니다. user 쿠키를 바꾸니, 내가 babo 라는 것을 서버가 알지 못합니다. 즉, user 쿠키는 현재 접속한 사용자가 누구인지 식별하는데에 사용됩니다.

이 가설은 실제로 사실입니다. (물론 babo 는 서버에 ssh 접속할 수 없으니 코드를 알지는 못합니다. 가설을 세우고 찍어서 맞춘 것입니다.)

```php
<!--page-babo.php -->
<?php
if ($_COOKIE["user"]=="babo_cookie") {
    echo "login success!";
} else {
    header("Location: goback.php");
    exit();
}
?>

```

# 추측2

babo 유저로 로그인했더니, 쿠키 이름이 babo_cookie 입니다.

그렇다면 grape 의 쿠키 이름은 grape_cookie 가 아닐까?

grape 의 개인페이지 이름도 page-babo.php 에서 page-grape.php 가 아닐까?

가설을 테스트해봅시다.

즉, 

- babo 로 로그인한다.
- Cookie Poisoning 을 이용하여 user 의 value 를 babo_cookie 에서 grape_cookie 로 변조한다.
- page-grape.php 에 접속을 시도한다.

순서입니다.

![Untitled](Untitled%20452.png)

![Untitled](Untitled%20453.png)

![Untitled](Untitled%20454.png)

![Untitled](Untitled%20455.png)

이런. 접속 성공했습니다.

- babo 는 grape 의 패스워드를 알지 못합니다.
- 쿠키 변조(Cookie Poisoning) 을 이용하여 자신의 쿠키를 바꿔  grape 의 개인페이지에 접속 성공했습니다.

# 보안 사고

해커 babo 는 보안 사고를 일으켰습니다.

다른 웹사이트, 예를들어 네이버나 구글 같은 웹사이트에 이러한 취약점이 있었다면, 

grape 의 개인페이지에는 다양한 기능이 있었을 것 입니다.

구글 드라이브에 접속하거나, 네이버 블로그에 이상한 글을 쓰거나 하는 것이 가능할 것 입니다.

이런 것을 보안 사고라고 부릅니다.

이 보안 사고의 원인이 된 취약점은 크게 두가지 입니다.

- Cookie 를 이용하여 중요한 기능을 처리
    - 쿠키는 Client-side 인 브라우저에서 손쉽게 변경이 가능하므로, 중요한 기능을 쿠키로 처리해서는 안됩니다.
- Cookie 의 Value 가 추측하기 쉬운 값임
    - 아이디가 babo 인데, 쿠키값이 babo_cookie 라면 규칙성이 뻔히 보입니다.
    - cindy라는 유저가 있는데, 쿠키값이 cindy_cookie 라면 이제 빼박입니다.

계속