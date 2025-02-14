# 7-2_Session_login : 세션 로그인

<aside>
💡 author : 전재호(agamtt) 2024-01-24
contributer : 박현준(Firebear518) 2024-04-07

</aside>

php 의 Session 기능을 이용해서 고양이 웹의 보안을 강화해봅시다.

우선, 현재 구현된 쿠키 방식의 index.php 의 로그인 기능을 살펴봅시다.

id 와 password 가 일치하는지 확인한 후, 일치하면 쿠키를 설정합니다.

```php
<!-- index.php -->
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST")
{    
    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    $grapeUsername = "grape";
    $grapePassword = "secret1234";

    $baboUsername = "babo";
    $baboPassword = "babo1234";

    if ($enteredUsername == $grapeUsername && $enteredPassword == $grapePassword)
    {
        setcookie("user", "grape_bs", time() + 3600, "/");
        header("Location: page-grape.php");
        exit();
    }
    else if ($enteredUsername == $baboUsername && $enteredPassword == $baboPassword)
    {
        setcookie("user", "babo_6GcT", time() + 3600, "/");
        header("Location: page-babo.php");
        exit();
    }
    else
    {
        $errorMessage = "Invalid username or password";
    }
}
?>
```

그리고, page-grape.php 엔드포인트에서 request 에 담긴 쿠키에 값을 확인하여 개인페이지를 보여줄지 말지 결정합니다.

```php
<!--page-grape.php -->
<?php
if ($_COOKIE["user"]=="grape_bs") {
    echo "login success!";
} else {
    header("Location: goback.php");
    exit();
}
?>
```

이것은 사용자가 쿠키를 조작할 수 있기 때문에 심각한 보안 결함을 가지고 있었습니다.

세션을 이용해 이를 보완해봅시다.

# php Session

php 에서 세션을 사용하려면, 먼저 session_start() 함수를 실행해야합니다.

session_start() 는, 세션이 없으면 생성하고, 세션이 있으면 해당 세션으로 부터 값을 읽어서 $_SESSION 변수에 저장합니다.

session_save_path() 는 세션파일을 어디에 저장할지 지정합니다.

```python
session_save_path('./');
session_start();
```

session_start() 를 실행하고 나면, $_SESSION 이라는 변수를 사용할 수 있습니다.

이 변수는 배열로, 세션파일을 읽고 쓸 수 있습니다.

아래 코드를 실행하면, 세션파일에 key:user 와 value:babo 가 저장됩니다.

쿠키와 달리, 이것은 서버에 있는 세션파일에 저장됩니다.

```php
$_SESSION['user'] = "babo"
```

# 코드에 적용

index.php 의 로그인 시스템을 아래와 같이 수정합니다.

```php
<?php

session_save_path('./');
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    $grapeUsername = "grape";
    $grapePassword = "secret1234";

    $baboUsername = "babo";
    $baboPassword = "babo1234";

    if ($enteredUsername == $grapeUsername && $enteredPassword == $grapePassword) {
        $_SESSION['user'] = "grape";
        header("Location: page-grape.php");
        exit();
    } elseif($enteredUsername == $baboUsername && $enteredPassword  == $baboPassword){
        $_SESSION['user'] = "babo";
        header("Location: page-babo.php");
        exit();
    } else {
        $errorMessage = "Invalid username or password";
    }
}
?>
```

babo 와 grape 의 개인페이지도 수정합니다.

```php
<!--page-babo.php -->
<?php
session_save_path('./');
session_start();

if (isset($_SESSION['user']) && $_SESSION['user'] == 'babo') {
    echo "login success!";
} else {
    header("Location: goback.php");
    exit();
}
?>
```

```php
<!--page-grape.php -->
<?php
session_save_path('./');
session_start();

if (isset($_SESSION['user']) && $_SESSION['user'] == 'grape') {
    echo "login success!";
} else {
    header("Location: goback.php");
    exit();
}

?>
```

# 테스트

이제 실행해보면,

PHPSESSID 라는 쿠키가 생기고 Value 가 난수값임을 알 수 있습니다.

(꽤 긴 난수니까 Brute Force 하기 어렵겠죠)

![Untitled](Untitled%20526.png)

서버에도 파일이 하나 생긴 것을 알 수 있습니다. 이것이 세션파일입니다.

- 클릭해서 열어보면, 내용은 비어있습니다.
- 파일이름이 브라우저의 쿠키값과 똑같습니다. 이것이 세션아이디입니다.

![Untitled](Untitled%20527.png)

이 세션쿠키와 세션파일은 index.php 의 session_start() 가 생성한 것입니다.

- 브라우저에는 세션쿠키를 생성하고 서버에는 세션파일을 생성합니다.
- 짝이되는 세션쿠키와 세션파일은 세션아이디가 똑같습니다.
- 이 경우 세션아이디는 h3d3j879945rhv7lm3d041tokr 입니다.

![Untitled](Untitled%20528.png)

session_start() 는 사용자의 request header 의 cookie 에 PHPSESSID 가 존재하지 않을 때와 존재할 때 다르게 동작합니다.

- PHPSESSID 가 존재하지 않으면 세션쿠키와 세션파일을 저장하고, 세션파일을 읽어서 $_SESSION 변수에 저장합니다
- PHPSESSID 가 존재하면 세션쿠키와 동일한 세션아이디를 가진 세션파일을 읽어서 $_SESSION 에 저장합니다.

# 로그인 기능

아래를 보면, 이미 session_start() 가 실행된 후이므로, 브라우저의 세션쿠키와 서버의 세션파일이 짝을 이루고 있습니다.

$_SESSION[’user’] = “grape” 가 실행되면 **세션파일에 user:grape 가 저장됩니다.**

```php
session_start();
...중략...
if ($enteredUsername == $grapeUsername && $enteredPassword == $grapePassword) {
        $_SESSION['user'] = "grape";
        header("Location: page-grape.php");
        exit();
```

관찰해봅시다.

아래 파일에 아무것도 없다가,

![Untitled](Untitled%20529.png)

grape로 로그인을 성공하면,

![Untitled](Untitled%20530.png)

동일한 Session ID 를 가진 (짝을 이루는) 세션파일에 key 와 value 가 기록됩니다.

![Untitled](Untitled%20531.png)

grape 의 개인페이지에서는 이 세션파일을 읽어서, 

user 의 값이 grape 인지 확인하여 인증합니다.

```php
session_start();
...중략

if (isset($_SESSION['user']) && $_SESSION['user'] == 'grape') {
    echo "login success!";
} else {
    header("Location: goback.php");
    exit();
}
```

# 결론

세션을 사용하면, 보안이 매우 향상 됩니다. 따라서 현대 웹페이지는 거의 모두 세션을 사용합니다.

- 접속하는 모든 사람은 세션을 부여받습니다. 인터넷에서, 세션은 나 그 자체 입니다.
- 세션쿠키는 세션파일을 찾는데에만 사용됩니다.
    - 조작해도 소용이 없습니다.
- 인증정보는 서버에 있는 세션파일에 저장되므로 조작이 불가능합니다.

그러나, 다음점을 유의해야합니다.

**“인터넷에서 세션은 나 그 자체입니다.”**

즉, 내가 아닌 다른 사람이 나의 세션값을 알게 되면, 그사람은 인터넷에서 **나인 행세**를 할 수 있습니다.

세션을 훔치는 해킹을 세션 하이재킹(Session Hijacking) 이라고 부릅니다.

계속