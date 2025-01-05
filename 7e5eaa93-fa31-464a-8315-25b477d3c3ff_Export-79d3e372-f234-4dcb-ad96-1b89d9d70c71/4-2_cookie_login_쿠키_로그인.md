# 4-2_cookie_login : 쿠키 로그인

<aside>
💡 author : 전재호(agamtt) 2023-01-10

</aside>

# http is stateless

<aside>
💡 웹은 http 를 이용하여 통신하는데, “http 는 stateless 하다” 라는 말을 코딩을 배우다 보면 듣게 될 것입니다. (아님말고)

</aside>

<aside>
💡 이것을 쉽게 이해하려면, stateless 의 반댓말인 statefull 한 통신이 뭐가 있는지 보면 됩니다.
ssh 는 statefull 합니다. 다음 명령어를 칠 때, 비밀번호를 새로 물어보지 않습니다. 당신을 기억하고 있습니다.

</aside>

<aside>
💡 http 는 stateless 하므로, 당신을 기억하지 않습니다.
웹페이지를 새로고침하면, 그저 새 request 신호가 서버로 전송됩니다.

</aside>

<aside>
💡 이것은 웹이 처음에, 단순히 검색이나 사전에 쓰였기 때문입니다. 하지만 앞서 말했듯이 접근을 제어하기 위해서는 사용자를 식별(identify)해야합니다. 이것에 쓰이는 웹브라우저의 기능을 cookie 라고 부릅니다.

</aside>

# Cookie

<aside>
💡 Cookie 는 “서버가 브라우저에 저장하도록 명령할 수 있는 변수” 기능입니다.

</aside>

서버의 php 에서 변수에 값을 지정하면, 이것은 서버 컴퓨터에 저장됩니다.

서버의 php 에서 쿠키에 값을 지정하면, 이것은 변수와 달리, 브라우저(클라이언트)에 저장됩니다.

쿠키를 이용해서 서버는 현재 접속한 브라우저가 누구인지 이름표를 달 수 있습니다.

# Cookie_login

index.php 의 php 코드 부분을 아래와 같이 수정합니다.

전:

```php
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    $validUsername = "grapeuser";
    $validPassword = "secret1234";

    if ($enteredUsername == $validUsername and $enteredPassword == $validPassword) {

        header("Location: login-success.php");
        exit();
    } else {
        $errorMessage = "Invalid username or password";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
...
```

후:

```php
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    $validUsername = "grapeuser";
    $validPassword = "secret1234";

    if ($enteredUsername == $validUsername && $enteredPassword == $validPassword) {

        setcookie("user", "grapeuser_cookie", time() + 3600, "/");
        header("Location: login-success.php");
        exit();

    } else {
        $errorMessage = "Invalid username or password";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
...중략

```

<aside>
💡 아래 코드는 로그인이 성공했을때, 서버가 브라우저에게, user 라는 이름의 cookie 의 값을 “grapeuser_cookie” 로 설정하도록 명령합니다.

</aside>

# 쿠키가 실제로 저장되었는지 확인하기

서버를 켜고, 자신의 웹포트로 접속합니다.

```php
php -S 0.0.0.0:80
```

![Untitled](Untitled%20421.png)

### 관리자 콘솔 열기

웹브라우저의 세부내용을 보는 기능을 **관리자 콘솔** 또는 **관리자 도구**라고 부릅니다. 

우클릭 후 “검사” 를 클릭하거나,

![Untitled](Untitled%20422.png)

F12 를 누르거나, Ctrl + Shift + J 를 누르면 관리자 콘솔이 열립니다.

![Untitled](Untitled%20423.png)

관리자 콘솔에서 Application > Cookies 를 클릭하여 현재 브라우저에 저장된 쿠키를 확인할 수 있습니다.

![Untitled](Untitled%20424.png)

<aside>
💡 우리가 백앤드에서, 로그인에 성공하면 쿠키가 저장되도록 해 두었습니다.
로그인을 해서 쿠키가 저장되는지 확인해봅시다.

</aside>

올바른 아이디와 패스워드를 입력합니다

![Untitled](Untitled%20425.png)

user 라는 쿠키이름에 Value 로 grapeuser_cookie 가 저장된 것을 확인할 수 있습니다.

![Untitled](Untitled%20426.png)

# Cookie 검사해서 튕겨내기

<aside>
💡 쿠키는 브라우저가 서버에 요청을 보낼때, 요청에 포함되어서 전송됩니다.

</aside>

<aside>
💡 즉, 서버는 요청에 포함된 쿠키를 읽고, 이 변수에 접근 가능합니다.

</aside>

login-success.php 을 아래와 같이 수정합니다.

전:

```php
<!DOCTYPE html>
<html lang="en">
<head>
...중략
```

후:

```php
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

$_COOKIE 는 http request 로 부터 온 사용자의 쿠키가 저장되어있는 배열입니다.

사용자의 쿠키가 저장된 배열에서 user 라는 이름의 쿠키가 존재하면 isset 이 True 입니다.

user 라는 이름의 쿠키가 존재하지 않으면, goback.php 라는 endpoint 로 redirect 합니다.

redirect 하고 나면 현재 코드는 종료시킵니다.

user 쿠키가 설정되어있지 않은 경우 redirect 되어 이동할 endpoint 도 만들어줍니다.

파일명 : goback.php

```php
<h1>You are not allowed to See this. go back.</h1>
```

![Untitled](Untitled%20427.png)

이제,  ID 와 PASSWORD 를 입력한 후 성공해서, 쿠키를 서버로부터 발급받지 않고,

곧장 login-success.php endpoint 로 이동하려고 하면,

goback.php 로 강제로 이동됩니다.

![Untitled](Untitled%20428.png)

잘 작동합니다.

# php cookie

php 는 $_COOKIE 라는 배열에 request 로 부터 온 쿠키를 저장합니다.

코딩해봅시다.

print_cookie.php 라는 파일을 생성하고 아래와 같이 코딩합니다.

```php
<?php
echo $_COOKIE;
?>
```

서버를 켜고 접속해보면,

![Untitled](Untitled%20429.png)

배열(Array) 이라고 뜹니다.

$_COOKIE 배열에서, user 라는 key 로 검색하도록 수정합니다.

```php
<?php
echo $_COOKIE['user'];
?>
```

우리가 세팅한 grapehacker_cookie 가 출력됩니다.

![Untitled](Untitled%20430.png)

![Untitled](Untitled%20431.png)

계속