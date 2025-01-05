# 5-3_cookie_auth_Mitigation : 쿠키값을 추측하기 어렵게 만들기

<aside>
💡 author : 전재호(agamtt) 2024-01-24

</aside>

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

# Mitigation : 추측하기 어려운 값

그렇다면, **쿠키값을 추측하기 어렵게 만드는 것**으로 이 공격을 막을 수 있을 것 같습니다.

랜덤한 값을 뒤에 붙여서요.

예를들어,

babo 의 user 쿠키의 값이 babo_cookie 가 아니라, babo_6GcT… 이고,

grape 의 user 쿠키의 값이 grape_cookie 가 아니라, grape_A8xK… 이면

babo 는 grape 의 쿠키에 있는 랜덤한 값인 A8xK 를 알 수 없으므로 Cookie Poisoning 공격을 할 수 없습니다.

코드를 수정해봅시다.

grape_cookie → grape_bs

babo_cookie → babo_dg

```php
<!-- index.php -->
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    $grapeUsername = "grape";
    $grapePassword = "secret1234";

    $baboUsername = "babo";
    $baboPassword = "babo1234";

    if ($enteredUsername == $grapeUsername && $enteredPassword == $grapePassword) {
        setcookie("user", "grape_bs", time() + 3600, "/");
        header("Location: page-grape.php");
        exit();
    } elseif($enteredUsername == $baboUsername && $enteredPassword  == $baboPassword){
        setcookie("user", "babo_dg", time() + 3600, "/");
        header("Location: page-babo.php");
        exit();
    } else {
        $errorMessage = "Invalid username or password";
    }
}
?>
```

그리고 각자의 페이지의 쿠키를 체크하는 인증 부분도 수정합니다.

babo_cookie → babo_dg 

```php
<!--page-babo.php -->
<?php
if ($_COOKIE["user"]=="babo_dg") {
    echo "login success!";
} else {
    header("Location: goback.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>grape cat web</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            background-color: #f4f4f4;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }

        main {
            padding: 20px;
            margin-bottom: 80px;
        }

        form {
            max-width: 400px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input {
            width: 100%;
            padding: 12px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            background-color: #333;
            color: #fff;
            cursor: pointer;
            padding: 12px;
            border: none;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input[type="submit"]:hover {
            background-color: #555;
        }

        footer, nav {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }
    </style>
</head>
<body>

    <header>
        <h1>개인 페이지</h1>
        <a href="logout.php"><h1>Logout</h1></a>
    </header>

    <main>
        <h2>안녕하세요 바보의 개인페이지입니다.</h2>
        <img src="https://item.kakaocdn.net/do/49a292677e5b578a8985bb315c19700c960f4ab09fe6e38bae8c63030c9b37f9" alt="바보">
        <h3><나의 사진> </h3>
        <h3>전화번호 : 010-TTTT-TTTT<h3>
        <h3>계좌번호 : 강아지은행 BBB-BBB-BBB<h3>    
    </main>

    <footer>
        <p>&copy; 2023 Your Website. All rights reserved.</p>
    </footer>

</body>
</html>
```

grape_cookie → grape_bs

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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>grape cat web</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            background-color: #f4f4f4;
        }

        header {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
        }

        main {
            padding: 20px;
            margin-bottom: 80px;
        }

        form {
            max-width: 400px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }

        input {
            width: 100%;
            padding: 12px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input[type="submit"] {
            background-color: #333;
            color: #fff;
            cursor: pointer;
            padding: 12px;
            border: none;
            border-radius: 4px;
            box-sizing: border-box;
        }

        input[type="submit"]:hover {
            background-color: #555;
        }

        footer, nav {
            background-color: #333;
            color: #fff;
            text-align: center;
            padding: 10px;
            position: fixed;
            bottom: 0;
            width: 100%;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }
    </style>
</head>
<body>

    <header>
        <h1>개인 페이지</h1>
        <a href="logout.php"><h1>Logout</h1></a>
    </header>

    <main>
        <h2>안녕하세요 grape 의 개인페이지입니다.</h2>
        <img src="https://img.segye.com/content/image/2017/08/30/20170830515039.jpg" alt="포도 사진">
        <h3><나의 사진> </h3>
        <h3>전화번호 : 010-XXXX-XXXX<h3>
        <h3>계좌번호 : 고양이은행 MMM-MMM-MMM<h3>    
    </main>

    <footer>
        <p>&copy; 2023 Your Website. All rights reserved.</p>
    </footer>

</body>
</html>
```

# 취약점 공격 시도 : Cookie Poisoning

![Untitled](Untitled%20460.png)

아 이런,

- 해커 babo 는 user 쿠키가 사용자 인증에 쓰인다는 것 까지는 추측으로 알아냈습니다.
- 그러나, 랜덤한 값이 뒤에 붙어있으므로, grape 유저의 **랜덤값을 쉽게 추측하지 못합니다.**
- 보안이 향상되었습니다.

많은 보안 기능들이 “**쉽게 추측하지 못하는 값**” 에 의존한다는 사실을 알아두시기 바랍니다.

이 사이트는 해킹으로 안전할까요?

… 두고 봅시다. babo 는 새로운 공격을 준비해서 해킹에 도전합니다.

계속