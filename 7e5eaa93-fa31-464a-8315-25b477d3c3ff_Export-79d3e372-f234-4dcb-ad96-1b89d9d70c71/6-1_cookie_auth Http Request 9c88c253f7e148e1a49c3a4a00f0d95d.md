# 6-1_cookie_auth : Http Request

<aside>
💡 author : 전재호(agamtt) 2024-01-24

</aside>

# index.php 에 접속하였을때 실제로 일어나는 일

사실 웹서버와 브라우저가 갠톡을 나눈 것과 같습니다.

Http 라는 규칙으로요. (이런 규칙을 통신 프로토콜이라고 부릅니다.)

브라우저가 하나 보내면, 웹서버도 하나 보냅니다.

 

그 카톡 내용을 까보면 이렇게 생겼습니다.

브라우저가 보낸 것은 Request, 서버가 보낸것은 Response 라고 부릅니다.

아래 사진에서, 좌측이 브라우저가 보낸 Request(요청) 이고,

우측이 서버가 보낸 Response(응답) 입니다.

![Untitled](Untitled%20461.png)

# 브라우저가 보낸 Request

아래 Login 버튼을 누르면,

![Untitled](Untitled%20462.png)

우리가 index.php 에 만든 form 이 작동됩니다.

```python
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
```

그러면 아래와 같은 선톡을 브라우저가 웹서버에게 보냅니다.

선톡을 보내다니 상남자네요

![Untitled](Untitled%20463.png)

# Request

<aside>
💡 request 는 브라우저가 보낸 선톡입니다.

</aside>

### Method

가장 앞에 나오는 POST 를 Http Method 또는 Method(메소드)라고 부릅니다.

![Untitled](Untitled%20464.png)

우리가 index.php 에서, form 클릭 시 POST method 로 request 를 전송하도록 해 두었기때문에, post request 가 전송되었습니다.

```python
... 중략
<form method="post">
        <?php
... 중략
```

POST method 는 일종의 글쓰기/편집 기능입니다.

웹서버에게, 단순한 요청이 아니라, 서버에 글이나 사진을 보낼거야 라고 알려주는 역할을 합니다. 일종의 첨부파일 기능인 것이죠

method 가 post 일때, 맨 아래에는 보낼 첨부파일이나 텍스트가 붙습니다.

이를 페이로드(payload) 또는 데이터(data) 라고 부릅니다.

우리가 만든 index.php 의 form 은 사용자가 username 과 password 를 form 에 입력하고 login 버튼을 누르는 순간 payload 에 이 값들이 담긴 post 요청을 서버로 전송합니다.

![Untitled](Untitled%20465.png)

만일 단순히 주소창에 주소를 입력하고 엔터를 치면 Method 가 GET 인 요청을 보냅니다.

그러면 웹서버는 아 전송할 데이터(payload)가 없구나, 라는 것을 알 수 있습니다.

![Untitled](Untitled%20466.png)

# Header (대갈통)

아래 보이는 Host, Content-Length … 를 모두 Header 라고 부릅니다.

Header 에는 브라우저가 보낸 다양한 정보가 담겨 있습니다.

![Untitled](Untitled%20467.png)

어떤 브라우저를 썼는지, 언어는 뭘 써야되는지 같은 내용이 담겨있습니다.

![Untitled](Untitled%20468.png)

# Response

<aside>
💡 브라우저가 request 를 보냈을 때, 서버가 보낸 답장을 Response(응답)이라고 부릅니다.
(물론 읽씹을 당할 수도 있습니다.)

</aside>

### 상태코드(status code)

Request 를 보냈을 때, 이 Request 가 잘 도착한건지, 잘 도착은 했는데 브라우저가 요구한 파일을 웹서버가 못찾은것인지, 웹서버가 답장해줍니다.

이것을 숫자로 보내는데, 이 숫자를 상태코드(status code) 라고 부릅니다

200 은 “Request 잘 받았고, 니가 요청한 파일도 찾았어” 라는 뜻 입니다.

![Untitled](Untitled%20469.png)

404 는 “Request 는 잘 받았는데, 니가 요청한 파일은 없는거같애” 라는 뜻 입니다.

아래를 보면, helloworld.php 를 Get 요청하면, 404 Not Found 라는 status code 가 답장옵니다.

![Untitled](Untitled%20470.png)

![Untitled](Untitled%20471.png)

# 쿠키가 세팅되는 과정

쿠키는 사실 웹서버가 보낸 Set-Cookie 헤더에 있는 내용을 브라우저가 적용하여서 저장됩니다.

우리가 웹서버의 백엔드에 아래와 같이 코딩하면, 브라우저가 POST 요청을 보냈을 때 if 문이 작동합니다.

```python
if ($_SERVER["REQUEST_METHOD"] == "POST") {

...중략...

$baboUsername = "babo";
    $baboPassword = "babo1234";

    if ($enteredUsername == $grapeUsername && $enteredPassword == $grapePassword) {
        setcookie("user", "grape_AxG4p", time() + 3600, "/");
        header("Location: page-grape.php");
        exit();
    }
```

setcookie 함수는 Response 의 Header 중 Set-Cookie 에 이를 담아서 전송합니다. 

아래를 보면, Set-Cookie : user=babo_6GcAE 로 설정해달라는 Response 를 서버가 보냈습니다.

![Untitled](Untitled%20472.png)

여기에는 언제까지 이 쿠키를 저장하고 삭제할 것인지에 대한 상세한 설정이 적혀있습니다.

이걸 들을지 말지는 브라우저가 정하는 것이지만…

![Untitled](Untitled%20473.png)

# 리다이렉트가 일어나는 과정

우리는 리다이렉트를 이용하여 로그인, 보안기능 등을 구현했습니다.

php 의 header 함수에 Location : 리다이렉트로 보낼 곳 이렇게 쓰면 거기로 이동됐었습니다.

외워서 그냥 코딩했었는데, 이제 이유를 설명할 수 있습니다.

```python
if ($enteredUsername == $grapeUsername && $enteredPassword == $grapePassword) {
        setcookie("user", "grape_AxG4p", time() + 3600, "/");
        header("Location: page-grape.php");
        exit();
```

다른 페이지로 이동되는 리다이렉트도 사실, 웹서버가 보낸 Response Header 를 통해 작동합니다.

웹서버가 답장하길, 너 여기로 리다이렉트해라. 라고 헤더에 써서 보내면,

브라우저는 그것을 읽어서 이동합니다.

리다이렉트의 상태코드는 302 입니다.

즉, php 의 header 라는 함수를 쓰면, 서버가 보낼 답장(Response)를 직접 편집할 수 있습니다.

웹브라우저는 자동으로 Location : page-grape.php 로 이동합니다.

 

![Untitled](Untitled%20474.png)

Http Request 를 자유자재로 다룰 수 있어야 웹을 완전히 해킹을 할 수 있습니다.

빨간색 박스를 치느라 힘들었으니 꼭 여러번 읽어서 완전히 숙달하시기 바랍니다.

계속