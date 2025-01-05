# 3-1_form_login : 폼 로그인 만들기

<aside>
💡 author : 전재호(agamtt) 2023-01-06

</aside>

# http request : GET 와 POST

<aside>
💡 웹브라우저의 주소창에 서버에 있는 어떤 파일을 요청하는 신호를 http request 라고 부른다.

</aside>

<aside>
💡 http request 는 **인터넷을 통해** 전달됩니다.

</aside>

http request 에는 두가지 종류가 있습니다.

# GET

get 은 뭔가를 가져오는 http request 입니다.

- “index.html 을 불러오기” 는 GET request 입니다.
- “검색하기” 는 GET request 입니다.

# POST

post 는 뭔가 서버에 쓰는 http request 입니다.

- “글쓰기” 는 POST request 입니다.
- “로그인 아이디와 로그인 패스워드 보내기” 는 POST request 입니다.

<aside>
💡 GET 과 POST 는 무 자르듯이 딱 나뉘는 것이 아닙니다. 개발자가 원하는대로 개발하는 것입니다.

</aside>

# POST 로 로그인 정보 받기

<aside>
💡 우리가 흔히 아는 “로그인 기능” 이라는 것은 다음과 같은 순서로 이루어집니다.

</aside>

- 브라우저에서 로그인 정보를 입력한다.
- 브라우저가 이를 서버에 전송한다.

<aside>
💡

우리는 url query 라는 것을 이용하여 로그인 기능을 구현할 것입니다.

</aside>

# HTML 의 form

<aside>
💡 게시판에 글을 쓰거나, 로그인을 할때  주소창에 써야한다면 매우 불편할 것 입니다. 이를 개선하기 위해, 웹개발자들은 form 이라는 것을 만들었습니다.

</aside>

무언가를 POST 로 서버에 제출하는 (예를 들면 로그인) 같은 기능은 아주 아주 자주 쓰이는 기능입니다.

따라서, 이를 편하게 수행할 수 있는 기능을 html 이 제공하는데, 이를 **form** 이라고 부릅니다.

html 에서는 모든 것이 꺽쇠로 둘러쌓인 **태그**입니다.

form 태그를 이용하여 form 을 만들 수 있습니다.

form 은 웹브라우저 화면에 글자를 입력할 수 있는 칸을 생성하고, 전송버튼을 누르면 이를 url query 에 넣어서 POST http request 를 보내줍니다.

# 로그인폼

<aside>
💡 원시인이 아니라면 아래와 같은 창을 많이들 봤을 겁니다. 이것이 로그인폼입니다.

</aside>

![Untitled](Untitled%20407.png)

html 에서 form tag 는 글쓰기, 로그인, 회원가입 등 다양한 용도로 쓰입니다.

form tag 를 로그인 아이디 패스워드를 입력받는 용도로 썼을때 이를 **로그인폼**이라고 부릅니다.

로그인폼은 아래와 같은 기능을 합니다.

- input 을 비워둔 상태에서 submit (전송)을 하면 경고를 띄웁니다.

![Untitled](Untitled%20408.png)

- type=password 인 input 란의 입력을 * 등으로 안보이게 표시합니다.

![Untitled](Untitled%20409.png)

# form 과 url query

다시 고양이 홈페이지로 돌아옵시다. 

```php
localhost:8000/index.html
```

![Untitled](Untitled%20410.png)

아이디와 패스워드를 입력하고 엔터를 누르면,

![Untitled](Untitled%20411.png)

![Untitled](Untitled%20412.png)

로그인 버튼을 누르면 url query 가 생성된다.

```
http://localhost:8000/?username=gaeun&password=babo
```

즉, form 이라는 것은 사실 url query 를 편하게 생성하기 위한 것임을 알 수 있다. **실제로 웹사이트에서 로그인 창을 비워두고 주소창에 직접 url query  를 입력해도 로그인할 수 있다.**

```html
<form>

			<label for="username">username</label>
			<input name="username" type="text">

			<label for="password">password</label>
			<input name="password" type="password">

			<input type="submit" value="로그인">

		</form>
```

# 로그인

<aside>
💡 우리는 url query 를 이용하여 로그인 기능을 구현할 것이다. 대부분의 웹사이트가 그렇게 한다.

</aside>

아마 여러분이 원시인이 아니라면 로그인이라는 말을 평소에 자주 쓸 것 이다.

웹사이트에서 아이디와 패스워드를 이용한 로그인은 다음을 의미한다.

<aside>
💡 1. 아이디와 패스워드를 url query 등을 이용하여 서버로 전송한다.
2. 서버에서 아이디와 패스워드를 서버에 등록된 아이디 패스워드와 비교해본다.
3. 로그인 시켜줄지 말지 결정한다.

</aside>

username 과 password 를 서버로 보내보자.

html 을 포함하는 php 파일을 만든다. 이제 index.html 은 필요없다. index.php 를 만들고, 고양이 홈페이지 html 을 넣은 후, php 와 html 을 함께 쓴다.

**index.php 를 만들고 index.html 은 지운다.**

<aside>
💡 .html 은 <?php 로 시작하는 php 스크립트를 실행하지 못한다. 이에 주의한다.
php 스크립트를 실행하려면 .php 파일이여야한다.

</aside>

index.php 에 이렇게 쓴다.

```php
<?php

$input_username = $_GET['username'];
$input_password = $_GET['password'];

echo "your name is $input_username,<br> and your password : $input_password "

?>

<html>
	<head>
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

		<form>
			<label for="username">username</label>
			<input name="username" type="text">
			<label for="password">password</label>
			<input name="password" type="password">
			<input type="submit" value="로그인">
		</form>

		<footer>
        <p>&copy; This is Cat Webpage. All rights reserved.</p>
    </footer>

	</body>
</html>
```

![Untitled](Untitled%20413.png)

서버에서 url query 를 통해 로그인 정보를 입력 받았다.

# 로그인 검증하기

이제 서버에서 이 로그인이 맞았는지를 확인할 것 입니다.

index.php 를 수정합시다.

우선, 우리의 로그인폼이 POST 요청을 보내도록 수정합니다.

이 폼은 POST request 를 전송하지 않습니다.

```php
<body>

		<header>
        <h1>GRAPE 고양이 웹</h1>
    </header>

		<form>
			<label for="username">username</label>
			<input name="username" type="text">
			<label for="password">password</label>
			<input name="password" type="password">
			<input type="submit" value="로그인">
		</form>

		<footer>
        <p>&copy; This is Cat Webpage. All rights reserved.</p>
    </footer>

</body>
```

아래와 같이 수정하면, POST request 를 전송합니다.

- form 안에 method 를 post 로 지정합니다.

```php
<body>

    <header>
        <h1>GRAPE 고양이 웹</h1>
    </header>

    <main>
        <form method="post">
            <h2>Login</h2>

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
```

이제 php 부분을 수정합니다.

아래는 단순히 입력받은 아이디와 비밀번호를 출력합니다.

```php
<?php

$input_username = $_GET['username'];
$input_password = $_GET['password'];

echo "your name is $input_username,<br> and your password : $input_password "

?>
```

아래와 같이 수정합니다.

- $_SERVER 는 서버로 받은 http request 를 저장되는 배열입니다.
- $_POST 는 받은 POST request 에 담긴 url query 가 저장되는 배열입니다.
- header() 를 이용하면 브라우저에게 명령을 보낼 수 있습니다.
    - 만일, 서버에 저장된 로그인 아이디와 패스워드가 POST request 에 들어있는 것과 동일하다면 if 문이 실행됩니다.
    - Location : endpoint 를 header 함수에 넣어서 해당 엔드포인트로 이동시킵니다.
    - 아이디와 패스워드가 틀리면 틀렸다고 알려줘야합니다.

<aside>
💡 아이디 패스워드는 그냥 grapeuser, secret1234 로 지정합니다.

</aside>

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

아이디나 패스워드가 틀리면 php 에서 $errorMessage 라는 변수에  “니 아이디 패스워드 마 틀렸다!” 라는 문자열이 저장됩니다.

- 이것을 html 의 로그인폼에서 출력하도록 만들면, 아이디와 비밀번호를 다시 입력하라는 기능을 구현할 수 있습니다.

아래와 같이 수정합니다

전:

```html

<form method="post">
          <h2>Login</h2>

          <label for="username">Username:</label>
          <input type="text" name="username" required>

          <label for="password">Password:</label>
          <input type="password" name="password" required>

          <input type="submit" value="Login">
 </form>
```

후:

- isset() 은 $errorMessage 라는 변수가 존재하는지 확인하는 함수입니다.
- php 태그를 삽입하여 $errorMessage 이 존재하는 경우에만 color : red 로 $errorMessage 를 출력합니다.

```php
<form method="post">
          <h2>Login</h2>

          <?php
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
```

여기까지 완성하고 실행합니다.

```html
php -S 0.0.0.0:80
```

틀린 로그인 정보를 입력하면,

![Untitled](Untitled%20414.png)

접속할 수 없다고 표시됩니다.

![Untitled](Untitled%20415.png)

코드에 있는 올바른 아이디 패스워드를 입력하면,

로그인됩니다.

![Untitled](Untitled%20416.png)

# 전체코드

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

위 사이트에는 **두가지 취약점**이 있습니다. 즉, 코딩을 바보같이 했다는 뜻입니다.

무엇인지 찾아보세요. 다음 페이지에서 다룹니다.

계속