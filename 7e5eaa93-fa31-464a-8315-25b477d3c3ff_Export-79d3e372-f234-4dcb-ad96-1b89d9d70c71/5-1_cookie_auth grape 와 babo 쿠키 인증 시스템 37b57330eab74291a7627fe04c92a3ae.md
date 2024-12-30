# 5-1_cookie_auth : grape 와 babo 쿠키 인증 시스템

<aside>
💡 author : 전재호(agamtt) 2024-01-24

</aside>

이제 쿠키를 이용하여 그럴싸한 로그인 인증 시스템을 만들어봅시다.

grape 와 babo 라는 두개의 유저를 만들고, 로그인 정보에 따라 다른 페이지로 이동하도록 만듭니다.

또한, 쿠키를 이용하여, grape 이외의 유저는 grape 의 개인페이지를 볼 수 없어야하고, babo 이외의 유저도 babo 의 개인페이지를 볼 수 없어야 합니다.

# php 에서 cookie 의 key 로 value 불러오기

아래와 같은 코드를 이용하여 key 로 value 를 불러올 수 있습니다.

```php
$_COOKIE["user"]
```

이것을 이용하여, 쿠키의 Value 에 따라 다르게 동작하도록 만들 수 있습니다.

```php
if ($_COOKIE["user"]=="grape_cookie"){
	//쿠키의 Value가 grape_cookie 인 경우 이 코드가 실행됨
}
```

이것을 각자의 개인페이지에 삽입하여서, user 쿠키의 value 에 따라 다르게 동작하도록 해봅시다.

index.php 를 아래와 같이 수정합니다.

validUsername 변수를, grapeUsername 과 baboUsername 으로 바꾸고,

validPassword 변수도, grapePassword 와 baboPassword 로 바꿉니다. 그리고 서로 다른 유저의 패스워드를 다르게 설정합니다.

그리고 login-success.php 를 두개의 유저에 대해 따로 만듭니다.

grape 로 로그인하면 page-grape.php 로 이동하고,

babo 로 로그인하면 page-babo.php 로 이동하도록 만듭니다.

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
        setcookie("user", "grape_cookie", time() + 3600, "/");
        header("Location: page-grape.php");
        exit();
    } elseif($enteredUsername == $baboUsername && $enteredPassword  == $baboPassword){
        setcookie("user", "babo_cookie", time() + 3600, "/");
        header("Location: page-babo.php");
        exit();
    } else {
        $errorMessage = "Invalid username or password";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Website</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            background-color: #f4f4f4;
        }

        header {
            background-color: #DE628B;
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
            background-color: #DE628B;
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
            background-color: #DE628B;
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
        <h1>GRAPE 고양이 웹</h1>
    </header>

    <main>

        <form method="post">

        <?php
            // Display error message if any
            if (isset($errorMessage)) {
                echo '<p style="color: red;">' . $errorMessage . '</p>';
            }
        ?>
            <h2>Login</h2>

            <label for="username">Username:</label>
            <input type="text" name="username" required>

            <label for="password">Password:</label>
            <input type="password" name="password" required>

            <input type="submit" value="Login">
        </form>

        <h2>Welcome to Your Website hello</h2>
        <p>This is a sample content for your website.</p>
    </main>

    <footer>
        <p>&copy; 2023 Your Website. All rights reserved.</p>
    </footer>

</body>
</html>
```

login-success.php 는 삭제하고,

page-grape.php 와

page-babo.php

두개의 파일을 생성합니다.

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

```php
<!--page-grape.php -->
<?php
if ($_COOKIE["user"]=="grape_cookie") {
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

로그아웃 기능도 만듭니다.

- 로그아웃 버튼을 누르면, logout.php 로 리다이렉트됩니다.
- logout.php 에서는 쿠키를 삭제하고 index.php 로 리다이렉트합니다.

```php
<!--logout.php-->

<h1>logout...</h1>

<?php

// delete cookie
setcookie('user', '', time() - 3600);

// Redirect to the login page
header("Location: index.php");
exit();
?>
```

잘못된 접근을 하였을 때, 접속하지 못하게 하는 goback.php 도 생성합니다.

```php
<!-- goback.php -->
<h1> 잘못된 접근입니다. Invalid Access. go back.</h1>

<img src="https://i.kym-cdn.com/photos/images/original/001/592/177/28c.png" alt="꺼지셈">
```

# 접속 테스트

잘 작동하는지 확인합니다.

폴더의 파일은 index.php, page-grape.php, page-babo.php, logout.php, goback.php 이렇게 존재해야합니다.

서버를 작동시킬 때, 반드시 해당 폴더에서 실행하였는지 확인하세요.

```php
php -S 0.0.0.0:80
```

처음 index.php 에 접속하면, 아무 쿠키도 저장되어있지 않습니다.

![Untitled](Untitled%20439.png)

Username 에 grape,

Password 에 secret1234 를 입력하면 grape 유저로 로그인되어 grape 의 개인페이지로 리다이렉트됩니다.

브라우저에는 key:user, value:grape_cookie 인 쿠키가 생성됩니다.

![Untitled](Untitled%20440.png)

로그아웃 버튼을 누르면 index.php 로 이동됩니다. user 쿠키는 삭제됩니다.

![Untitled](Untitled%20441.png)

![Untitled](Untitled%20442.png)

만일,

Username 에 babo,

Password 에 babo1234 를 입력하면

babo 의 개인페이지로 리다이렉트 됩니다.

![Untitled](Untitled%20443.png)

# 보안 기능 테스트

<aside>
💡 babo 는 grape 의 개인페이지를 볼 수 없어야 합니다.

마찬가지로, grape 도 babo 의 개인페이지를 볼 수 없습니다.

babo 는 grape 의 개인정보를 침해하기 위하여 page-grape.php 로 접속하려고 합니다.

</aside>

로그인한 유저가 babo 이면, user 쿠키의 value 가 babo_cookie 로 설정되어있습니다.

이 상태에서, page-grape.php 를 주소창에 입력해서 접속하려고 한다면,

![Untitled](Untitled%20444.png)

page-grape.php 에 있는 아래 코드가 작동합니다.

- user 쿠키의 value가 grape_cookie 가 아니기 때문에, else 문이 실행됩니다.
- goback.php 로 리다이렉트 됩니다.

```php
<!--page-grape.php -->
<?php
if ($_COOKIE["user"]=="grape_cookie") {
    echo "login success!";
} else {
    header("Location: goback.php");
    exit();
}
?>

```

goback.php 로 강제 리다이렉트 됩니다.

![Untitled](Untitled%20445.png)

이런. 이제 user 라는 쿠키가 있어도, 그 값에 따라 다른 페이지로 이동됩니다.

grape 의 전화번호와 계좌번호는 잘 지켜질 것 입니다.

…과연 그럴까요?

grape 의 개인페이지를 해킹해보겠습니다.

계속