# 4-3_cookie_login_Hacking : Client-side Cookie Poisoning

<aside>
💡 author : 전재호(agamtt) 2024-01-23

</aside>

# Poisoning

Poisoning 은 위조,변조 라는 뜻 입니다.

사이버 보안에서 무언가를 Poisoning 한다는 것은 어떤 값을 바꿔서 속이는 행위를 말합니다.

# Client-Side Cookie Poisoning

Cookie 는 **사용자의 브라우저에 저장되는 변수입니다.**

즉, 사용자가 마음대로 값을 삭제하거나 바꿀 수 있습니다.

이를 간과하는 것은 아주 큰 보안 위험이 될 수 있습니다.

웹은 클라이언트와 웹이 통신하는 구조로 되어있습니다.

브라우저나 앱 등, 사용자가 사용하는 쪽을 Client-Side 라고 부릅니다.

Client-Side 에서 Cookie 를 조작하는 해킹기법을 Cookie Poisoning 이라고 부릅니다.

# Cookie Poisoning Bypass Auth

우리가 만든 고양이 홈페이지는 로그인-인증을 쿠키로 검증하는 시스템입니다.

그러나, 쿠키는 사용자가 마음대로 삭제하거나 바꿀 수 있으므로, 보안상 취약합니다.

이를 해킹해서, 비밀번호를 모르는 상태에서 로그인 해보겠습니다.

이렇게, 어떤 보안시스템(이 경우, 비밀번호 인증)을 우회하는 것을 **Bypass** 라고 부릅니다.

저번시간에 만든 고양이 홈페이지의 보안시스템을 확인해봅시다.

### index.php

- 사용자가 아이디와 패스워드를 입력하여, 인증에 성공하면 user = grapehacker_cookie 로 쿠키를 저장합니다.
- 아닌 경우, Invalid username or password 를 표시합니다.

```nasm
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    $validUsername = "grapeuser";
    $validPassword = "secret1234";

    if ($enteredUsername == $validUsername && $enteredPassword == $validPassword) {

        setcookie("user", "grapeuser_cookie", time() + 3600, "/");

        if (isset($_COOKIE["user"])) {
            echo "Cookie Value 'user': " . $_COOKIE["user"];
        } else {
            echo "there is no cookie!";
        }
        header("Location: login-success.php");
        exit();

    } else {
        $errorMessage = "Invalid username or password";
    }
}
?>
```

### login-success.php

- $_COOKIE 배열에는 request 에 포함된 쿠키가 배열로 저장되어있습니다.
- $_COOKIE[”user”] 는 key=user 인 쿠키를 검색합니다.
    - 로그인에 성공했을때에만 key:user, value:grapeuser_cookie 가 저장됩니다.
    - isset 은 변수가 있는지 없는지 확인하는 함수입니다.
- user 쿠키가 없으면, goback.php 로 리다이렉트 시킵니다.
    - user 쿠키가 없으면, login-success.php 에 접근할 수 없습니다.

```nasm
<?php
if (!isset($_COOKIE["user"])) {
    header("Location: goback.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
...중략
```

보안시스템을 확인해봅시다.

만일, user 쿠키가 없는 상태에서 login-success 에 접근하면,

![Untitled](Untitled%20432.png)

goback.php 로 리다이렉트됩니다. 로그인할 수 없습니다….

비밀번호를 알아야만 접속할 수 있겠군요….

![Untitled](Untitled%20433.png)

**그렇지 않습니다.**

해킹해봅시다.

# Hacking : 개발자 콘솔을 이용한 방법

그렇다면, user 쿠키가 존재하기만 하면 로그인에 성공합니다.

쿠키는 브라우저에 있으므로, 얼마든지 편집할 수 있습니다.

브라우저에서 Ctrl+Shift+J 를 눌러서 개발자 콘솔을 엽니다.

![Untitled](Untitled%20434.png)

Application/Cookies 에서 쿠키를 확인할 수 있습니다.

![Untitled](Untitled%20435.png)

![Untitled](Untitled%20436.png)

키를 user 로 하고, value 는 아무거나 쓰고 저장합니다.

![Untitled](Untitled%20437.png)

goback.php 로 리다이렉트되지 않고 로그인에 성공합니다.

![Untitled](Untitled%20438.png)

grapeuser 의 전화번호와 계좌번호를 효과적으로 탈취했습니다.

끝