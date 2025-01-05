# 3-2_form_login Hacking : Broken Access Control Vulnerability

<aside>
💡 author : 전재호(agamtt) 2023-01-06

</aside>

# 이전 시간 전체 코드

index.php

```php
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    $validUsername = "grapeuser";
    $validPassword = "secret1234";

    if ($enteredUsername == $validUsername or $enteredPassword == $validPassword) {

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
            <h2>Login</h2>

            <?php
            // Display error message if any
            if (isset($errorMessage)) {
                echo '<p style="color: red;">' . $errorMessage . '</p>';
            }
		        ?>

            <label for="username">Username:</label>
            <input type="text" name="username" required>

            <label for="password">Password:</label>
            <input type="password" name="password" required>

            <input type="submit" value="Login">
        </form>

    </main>

    <footer>
        <p>&copy; 2023 Your Website. All rights reserved.</p>
    </footer>

</body>
</html>
```

login-success.php

```php
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
        <h2>안녕하세요 당신의 개인페이지입니다.</h2>
        <img src="https://placekitten.com/200/200" alt="고양이 사진">
        <h3><나의 고양이> </h3>
        <h3>전화번호 : 010-1234-1234<h3>
        <h3>계좌번호 : 12341234<h3>    
    </main>

    <footer>
        <p>&copy; 2023 Your Website. All rights reserved.</p>
    </footer>

</body>
</html>
```

위 사이트에는 **두가지 취약점**이 있습니다. 즉, 코딩을 **같이 했다는 뜻입니다.

# 취약점(Vulnerability)

- 취약점은, 코딩을 이상하게 했다던지, 다양한 실수로 부터 발생하는 시스템의 약점입니다.
- 해커는 이 취약점을 공략해서 여러가지 악성행위를 할 수 있습니다.
- 개발자는 이러한 취약점을 해커보다 먼저 찾아내서 고쳐야 합니다.
- 해커는 개발자보다 먼저 취약점을 찾아내서, 이를 악용합니다.

# Broken Access Control Vulnerability

<aside>
💡 Broken Access Control 은 **손상된 접근제어**라는 뜻 입니다.

</aside>

로그인과 같이, 특정 기능을 정해진 유저만 수행할 수 있도록 제한하는 것을 **접근제어**라고 부릅니다.

특정 취약점은 접근제어를 손상시킵니다, **정해지지 않은 유저도, 해당 기능에 접근할 수 있게 됩니다.**

이를 이용해서 grapeuser 의 로그인 페이지를 해킹해봅시다.

# 취약점 1 : or → and

잘 보면, 로그인 아이디와 패스워드를 검증하는 코드를 병신같이 짰습니다.

```php
<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    $validUsername = "grapeuser";
    $validPassword = "secret1234";

    if ($enteredUsername == $validUsername or $enteredPassword == $validPassword) {

        header("Location: login-success.php");
        exit();
    } else {
        $errorMessage = "Invalid username or password";
    }
}
?>
```

어!! 어!! 이부분입니다.

```php
if ($enteredUsername == $validUsername or $enteredPassword == $validPassword) {
```

로그인 성공하려면 아래 두 조건을 둘다 만족해야합니다.

- 아이디가 서버에 저장된 것과 동일
- 패스워드가 서버에 저장된 것과 동일

or 는 양쪽 조건중, **한가지 조건만 만족해도 if 문을 실행시킵니다.**

물론 뇌가 있으면 이렇게 코딩하지는 않겠지요? (교육을 위해 제가 의도적으로 취약하게 코딩했습니다)

# 취약점 악용(exploit)

이 취약점을 악용해봅시다.

or 로 논리문이 연결되어있으므로, 두 조건중 하나만 만족해도 됩니다.

- 아이디가 서버에 저장된 것과 동일
- 패스워드가 서버에 저장된 것과 동일

즉, **비밀번호를 모르고 아이디만 알아도 grapeuser 의 개인페이지에 접근할 수 있습니다.**

아이디는 grapeuser 를 입력하고, 패스워드는 아무거나 입력합니다.

![Untitled](Untitled%20417.png)

grapeuser 의 개인페이지에 접속 성공합니다.

**개발자가 의도하지 않은대로 웹을 이용했습니다.**

![Untitled](Untitled%20418.png)

# 취약점 2 : 엔드포인트 접근 손상

우리는 login-success.php 라는 엔드포인트가 있다는 것을 알고 있습니다.

그러니, **로그인하지말고, 그냥 url 을 이용해서 해당 엔드포인트에 접근합시다.**

아래 url 을 입력합니다

```php
{서버주소}/login-success.php
```

![Untitled](Untitled%20419.png)

아이디 패스워드 입력없이, 개인페이지에 접속합니다.

![Untitled](Untitled%20420.png)

grapeuser 의 개인페이지에 접속 성공합니다.

**개발자가 의도하지 않은대로 웹을 이용했습니다.**

<aside>
💡

그러나 엔드포인트의 이름을 알 수 없습니다.

</aside>

<aside>
💡 실제 해킹 상황이면 다음과 같이 할 수 있습니다. 임의의 다른 유저, 예를 들어, jeho 로 로그인 한 후, login-success 라는 엔드포인트가 존재함을 알아냅니다. 그 이후, grapeuser 의 개인페이지를 해킹할 수 있습니다.

</aside>

<aside>
💡 모든 엔드포인트의 이름의 경우의 수를 시도하면서 http request 를 보내, 엔드포인트를 알아내는 것을 endpoint brute force 공격이라고 부릅니다. 그러한 공격도구를 파이썬, Perl 등의 스크립트 언어로 제작할 수 있습니다. 또한 이미 그런 공격을 수행하는 도구가 세상에 많이 개발되어있습니다.

따라서 쉽게 추측할 수 없는 엔드포인트 이름을 사용하는 것이 안전합니다.

</aside>

# 취약점 패치(patch)

<aside>
💡 취약점을 고치는 것을 취약점 패치라고 부릅니다.
보안 패치라고도 부릅니다.

</aside>

우선 아래 코드의 or 을 and 로 바꿔야합니다. 둘다 만족해야, if문이 실행되도록 해야합니다.

전:

```php
    if ($enteredUsername == $validUsername or $enteredPassword == $validPassword) {
```

후:

```php
    if ($enteredUsername == $validUsername and $enteredPassword == $validPassword) {
```

엔드포인트 취약점을 수정하려면, 사용자를 **식별**해야합니다.

이러한 기능을 쿠키(Cookie) 라고 부릅니다.

이것을 다음 페이지에서 배워봅시다.

계속