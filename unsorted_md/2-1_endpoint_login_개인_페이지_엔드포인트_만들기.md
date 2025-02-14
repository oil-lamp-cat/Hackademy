# 2-1_endpoint_login : 개인 페이지 엔드포인트 만들기

<aside>
💡 author : 전재호(agamtt) 2023-01-06
contributor : 손기민(KiminSon) 2024-04-07

</aside>

# 엔드포인트

<aside>
💡 웹사이트는 대부분 여러개의 페이지를 포함하고 있습니다. 버튼을 클릭하거나 하여 이 페이지를 이동하며 웹서핑을 합니다.

</aside>

<aside>
💡 이러한 여러개의 페이지는 사실 여러개의 파일이며, 각각의 파일을 **엔드포인트**라고 부릅니다.

</aside>

# 고양이 개인페이지 엔드포인트 만들기

파일을 하나 더 생성해서 개인페이지를 만들어봅시다.

아래 파일을 생성합니다.

파일의 이름은 login-success.html입니다.

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

이제 다시 서버를 켜고, 해당 엔드포인트로 접속이 되는지 확인합니다.

이제 url 에 / (slash 라고 읽습니다) 로 해당 엔드포인트의 이름 (파일의 이름)을 입력하면 해당 페이지에 접속할 수 있습니다.

![Untitled](Untitled%20398.png)

/ 만 입력하면, 별다른 엔드포인트를 명시하지 않았으므로 index 라는 이름을 가진 엔드포인트를 불러옵니다. 

<aside>
💡 index 라는 엔드포인트는 전세계 웹의 표준 규격입니다. (물론 php 설정에서 바꿀 수 있습니다. 하지만 굳이?)

</aside>

이러한 / 엔드포인트를 “최상위 엔드포인트” 또는 “루트 엔드포인트” 라고 부릅니다.

우리의 루트 엔드포인트는 고양이 웹 로그인 페이지입니다.

![Untitled](Untitled%20399.png)

# 엔드포인트를 버튼과 연결하기

- login-success 엔드포인트로 접속하기 위해서 주소창에 엔드포인트이름을 입력해야한다면 매우 불편할 것 입니다.
- 어떤 이름의 엔드포인트가 있는지 사용자가 어떻게 알고 그걸 입력해?

<aside>
💡 따라서 (대부분의 웹사이트는) **html 요소**를 **엔드포인트와 연결**해둡니다. 이것을 **하이퍼링크**라고 부릅니다. (HTTP 는 하이퍼 링크 텍스트 프로토콜의 약자입니다!)

</aside>

index.html 코드의  body 태그를 아래와 같이 수정합니다.

```php
	<body>

		<header>
        <h1>GRAPE 고양이 웹</h1>
    </header>

	<form method="post">
		<h2>Login</h2>

		<label for="username">Username:</label>
		<input type="text" name="username" required>

		<label for="password">Password:</label>
		<input type="password" name="password" required>

		<input type="submit" value="Login">
	</form>
		  
		  <a href="/login-success.html">개인페이지로 이동</a>

		<footer>
        <p>&copy; This is Cat Webpage. All rights reserved.</p>
    </footer>

	</body>
```

그러면 개인페이지로 이동이라는 태그가 생깁니다. a 는 클릭할 수 있는 태그입니다. href 는 하이퍼 레퍼런스의 약자로, 해당 태그를 클릭하면 해당 엔드포인트로 이동합니다.

![Untitled](Untitled%20400.png)

클릭하면 로그인 성공 페이지로 이동됩니다.

![Untitled](Untitled%20401.png)

그러나, 개인페이지 (로그인 성공페이지) 라는 것은, 아무나 이동하면 안됩니다.

아래와 같이 작동해야합니다.

- 아이디 패스워드, 휴대폰 인증 등을 통해 현재 접속을 시도하고 있는 사람을 **식별(identify)**한다.
    - 개인페이지에 접속할 수 있는 사람은 엔드포인트로 이동시킨다.
    - 그외의 사람은 엔드포인트로 이동시키지 않는다
        - 아이디 또는 비밀번호가 틀렸습니다.

이러한 기능을 **로그인 기능**이라고 부릅니다.

<aside>
💡 html 은 프로그래밍 언어가 아닙니다. 이러한 논리적인 작동을 할 수 없습니다. 그저 화면을 만들고, 엔드포인트끼리 링크로 연결할 수 있는 기능만 가지고 있습니다.

</aside>

<aside>
💡 웹 개발자한테 html 이 프로그래밍 언어 아닌가요? 라고 부르면 **화가 날 수도 있습니다!**

</aside>

![이건 못참는다.](Untitled%20402.png)

이건 못참는다.

이러한 기능은 컴퓨터에서 코드로 수행되어야합니다.

**즉, 코딩을 해야합니다.**

이제, **php 로 코딩을 해봅시다.**

계속