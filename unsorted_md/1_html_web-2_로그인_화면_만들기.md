# 1_html_web-2  : 로그인 화면 만들기

<aside>
💡 author : 전재호(agamtt) 2023-12-05

</aside>

<aside>
⚠️ 우리는 해커지, 웹디자이너가 아니므로, 그냥 복붙하면서 변해가는 과정만 구경하면 됩니다.

</aside>

## 태그는 태그안에 들어갈 수 있다.

```html
<h1>
	<p> 이 문장은 h1 태그 안에있는 p 태그 문장입니다. </p>
</h1>
```

# head 태그와 body 태그

대부분의 웹페이지는 head 태그와 body 태그로 나눠집니다.

head 태그에는 페이지의 설정값을 모아둡니다.

언어 설정이나 그런겁니다. 걍 복붙하면 됨.

body 에는 페이지의 내용이 들어갑니다.

이 틀 안에다가 이제 문서를 만들 것 입니다.

```html
<html>
	<head>
	</head>
	<body>
	</body>
</html>
```

<aside>
💡 React 뭐 Vue 서블릿 컨테이너 같은 것도 마지막에는 결국 index.html 을 생성해서 보여줍니다. 
톰캣 서블릿 컨테이너 = JAVA 로 html 만들기
React = nodeJS 로 html 만들기

(*못들어봤다면 무시하시오.)

</aside>

## form

form 은 뭐 이런걸 말합니다.

![Untitled](Untitled%20386.png)

![Untitled](Untitled%20387.png)

![Untitled](Untitled%20388.png)

이런 form 은 거의 모든 웹사이트가 가지고 있고, 작동이 거의 비슷합니다.

그래서 form 태그라는 것으로 만들기로 전세계 사람들이 약속되어 있습니다.

<aside>
💡 form 이 무엇인지 나중에 자세히 배움. 지금은 복붙할 것

</aside>

## 참고 : 패스워드 매니저 (암호 자동완성기)

이런걸 본적이 있을 것 입니다.

![Untitled](Untitled%20389.png)

![Untitled](Untitled%20390.png)

이런 것은 브라우저가 제공하는 비밀번호 저장 기능인데, form 태그를 주로 아이디 패스워드 입력에 쓰다보니 form 태그가 있고, 거기에 두개의 값을 입력하는 어떤 구조를 찾으면 아이디 패스워드를 저장합니다.

<aside>
💡 **참고**
아이디 패스워드 입력기능을, form 태그로 안만들 수도 있습니다.
근데 그러면 다들 “표준을 안지키는 쓰레기 웹사이트라 비번 저장도 안된다”고 욕 합니다.

</aside>

우리의 고양이 웹사이트는 로그인 기능을 가지고 있습니다.

이 로그인을 위해 form 을 만들어줍니다.

index.html

```html
<html>
	<head>
	</head>
	<body>
		<h1>고양이 네이버</h1>
		<form>
			<input>
			<input>
		</form>
	</body>
</html>
```

그러면 뭔가 두개 생깁니다.

![Untitled](Untitled%20391.png)

글씨를 쓸 수도 있습니다. 와 짱이다

![Untitled](Untitled%20392.png)

하지만 어디가 아이디 패스워드인지 모르니 써둡시다.

label 은 form 입력칸에 이름을 붙이는 태그입니다. 어떤 form 인지 지정해야하니 name 을 통일해야합니다.

```html
<html>
	<head>
	</head>
	<body>
		<h1>고양이 네이버</h1>
		<form>
			<label for="username">username</label>
			<input name="username">
			<label for="password">password</label>
			<input name="password">
		</form>
	</body>
</html>
```

![Untitled](Untitled%20393.png)

근데 패스워드가 다 보입니다. *** 로 보이면 좋겠습니다. 그건 type을 지정하면 됩니다.

(아이디는 딱히 보여도 상관없으니 text 로 하면 됨)

```html
<html>
	<head>
	</head>
	<body>
		<h1>고양이 네이버</h1>
		<form>
			<label for="username">username</label>
			<input name="username" type="text">
			<label for="password">password</label>
			<input name="password" type="password">
		</form>
	</body>
</html>
```

잘 됩니다.

![Untitled](Untitled%20394.png)

로그인을 시도할 버튼이 있어야되니까 추가해준다. type 을 submit 으로 하면 된다. value 는 버튼안에 무슨 문자열을 넣을거냐를 정한다.

```html
<html>
	<head>
	</head>
	<body>
		<h1>고양이 네이버</h1>
		<form>
			<label for="username">username</label>
			<input name="username" type="text">
			<label for="password">password</label>
			<input name="password" type="password">
			<input type="submit" value="로그인">
		</form>
	</body>
</html>
```

![Untitled](Untitled%20395.png)

이제 헤더와 푸터를 만든다. 헤더는 맨위에 로고랑 막 있는 그거고 푸터는 맨 아래에 있는 그 링크 모여있는 그거임.

대충 있어보이게 쓰면 된다.

```html
<html>
	<head>
	</head>
	<body>

		<header>
        <h1>고양이 네이버</h1>
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

## 접속 테스트

<aside>
💡 접속해서 테스트해본다.

</aside>

<aside>
💡 php -S 0.0.0.0:80 는 반드시 index.html 이 있는 디렉토리에서 실행해야함!

</aside>

<aside>
💡 본인 컴퓨터에서 코딩한 경우, php -S 0.0.0.0:80 을 터미널에서 실행한 후, 웹브라우저 주소창에 [localhost](http://localhost) 입력

</aside>

<aside>
💡 서버의 도커 컨테이너에서 코딩한 경우, php -S 0.0.0.0:80 을 서버의 터미널에서 실행한 후, 웹브라우저 주소창에 서버주소:{80과 포트포워딩된 외부포트} 입력

</aside>

<aside>
💡 방학반의 경우, 도커 컨테이너에 접속하여 php -S 0.0.0.0:80 를 입력 후, [grape.iptime.org:9028](http://grape.iptime.org:9028) 를 웹브라우저 주소창에 입력
(9028 은 본인의 웹 포트로 바꾸기!)

</aside>

![Untitled](Untitled%20396.png)

아직은 이딴게 웹사이트인건지 모르겠는 수준이다.

꾸며주면 그럴싸해진다.

끝

전체코드

```python
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