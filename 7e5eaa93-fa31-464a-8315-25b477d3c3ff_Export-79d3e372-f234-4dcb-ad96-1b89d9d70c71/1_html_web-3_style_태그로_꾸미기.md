# 1_html_web-3: style 태그로 꾸미기

<aside>
💡 author : 전재호(agamtt) 2023-12-05

</aside>

<aside>
⚠️ 우리는 해커지, 웹디자이너가 아니므로, 그냥 복붙하면서 변해가는 과정만 구경하면 됩니다.

</aside>

index.html 을 여기까지 만들었다.

```html
<html>
	<head>
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

head 에는 여러가지가 들어가지만, style 이라는 태그가 들어간다. style 태그는 웹페이지를 예쁘게 만든다.

<aside>
⚠️ **귀찮**

시간 관계상 (귀찮다는 뜻) 디자인은 아래 코드를 그냥 복붙하기 바란다.
예쁘게 만들어도 못생기게 만들어도 웹사이트의 기능은 동일하다.
필자는 chatGPT 에게 디자인을 시켰다.
디자인에 관심이 있다면 웹디자인에 대해 찾아보기 바란다.

</aside>

```html
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

그럴싸해졌다

![Untitled](Untitled%20397.png)

계속