# 6-2_cookie_auth : requests.py

<aside>
💡 author : 전재호(agamtt) 2024-01-24
contributor : 손기민(KiminSon) 2024-04-08

</aside>

# requests.py

웹브라우저는 url 을 주소창에 입력하여 Http Request 를 보내는 프로그램이라는 것을 배웠습니다.

그러나, Http Request 를 보낼 수 있는 방법이 웹브라우저를 이용하는 방법밖에 없는 것은 아닙니다.

requests.py, curl, wget, HttpURLConnection.java 등을 이용하면 프로그래밍을 이용하여 Http request 를 보낼 수 있습니다.

우리는 파이썬을 배웠으므로, requests.py 를 이용하도록 합시다.

requests.py 는 파이썬으로 Http request 를 보낼 수 있도록 하는 파이썬 라이브러리입니다.

브라우저는 해킹을 위해 만들어진 물건이 아니므로,

Http Request 를 자유자재로 컨트롤하기 위해서는 직접 request 를 보내야 합니다.

바로 다음 해킹 공격에 필요하므로, 개념을 공부해보록 하겠습니다.

당최, Http Request 라는 것은 어떻게 생겨먹은 놈인지 알아야 합니다.

# 파이썬 코딩하기

새폴더를 만들고, Visual Studio Code 등 좋아하는 파이썬 에디터로 poc.py 라는 파일을 생성하여 빈 코드를 열어줍니다.

<aside>
⚠️ 새폴더를 만들고 코드파일을 생성하여 에디터로 확인할 수 없으면, 이 강의를 듣고 있으면 안됩니다!

</aside>

하지만… 친절하게 적도록 하겠습니다. 아유귀찮아

![Untitled](Untitled%20475.png)

![Untitled](Untitled%20476.png)

![Untitled](Untitled%20477.png)

![Untitled](Untitled%20478.png)

# index.php 에 get 요청 보내기

get 요청을 보내는 함수는 requests.get 입니다.

url 매개변수에 요청을 보낼 웹서버의 주소를 적습니다.

import requests에서 에러가 난다면 파이썬에서

```python
 pip install requests
```

명령어를 통해 라이브러리를 다운받고 하면 됩니다.

```python
import requests

url = 'http://localhost:8000/index.php'

response = requests.get(url)

print(response)
```

![Untitled](Untitled%20479.png)

<Response [200]> 이 표시됩니다.

200 이라는 숫자는 상태코드(status code) 를 의미합니다. 200은 정상적으로 요청이 도착했다는 뜻입니다.

만일 존재하지않는 엔드포인트로 요청을 보낸다면, 그런 엔드포인트를 찾지 못할 것입니다.

요청이 실패하면, 404 상태코드가 도착합니다.

none 이라는 엔드포인트로 바꿔서 요청을 보내보면, 404 가 도착합니다.

![Untitled](Untitled%20480.png)

상태코드가 200이라면, 도착한 response 에는 요청한 파일(index.php) 이 들어있습니다.

response.text 를 print 하면 볼 수 있습니다.

```python
import requests

url = 'http://localhost:8000/index.php'

response = requests.get(url)

print(response.text)
```

![Untitled](Untitled%20481.png)

이것은 우리가 백앤드에 코딩한, 서버가 보낸 파일이라는 것을 알 수 있습니다.

# index.php 에 post 요청 보내기

post 요청은 get 요청과 달리 payload 가 존재합니다.

```python
import requests

url = 'http://localhost:8000/index.php'
payload = {'username': 'grape', 'password': 'secret1234'}

response = requests.post(url, data = payload)

print(response.text)
```

# 고양이 웹의 Http request 확인하기

개발자 콘솔(웹브라우저에서 Ctrl+Shift+J 또는 F12) 의 Network 탭으로 이동하면 웹서버와 브라우저가 주고받은 Http request 를 볼 수 있습니다.

고양이 웹서버와 웹브라우저가 주고받은 Http Request 를 확인해봅시다.

goback.php 에 접속한 후, Headers 를 확인해보면,

접속을 요청한 url 과 상태코드(status code), Post 요청의 Payload 등을 알 수 있습니다.

index.php 엔트포인트는 post 요청을 받아 아이디와 패스워드를 입력받습니다.

![Untitled](Untitled%20482.png)

아이디와 패스워드에 아무 값이나 입력한 후, 클릭해서 Payload 를 확인해보면 아이디와 패스워드가 들어있습니다.

![Untitled](Untitled%20483.png)

goback.php 엔드포인트는 get 요청을 받아 goback.php 와 죽빵을 날리는 개구리 사진을 보내줍니다.

- get 요청이라서 payload 가 없습니다.
- 200 상태코드를 받았습니다.

![Untitled](Untitled%20484.png)

# requests 로 고양이 웹에 요청 보내기

다시 파이썬 코드로 돌아와서 코드를 짜봅시다.

### get 요청 보내기

우선, goback.php 에 get 요청을 보내봅시다.

```python
''' req_goback.py '''
import requests

url = 'http://localhost:8000/goback.php'

response = requests.get(url)

print(response)
print(response.text)
```

response 가 오는 것을 확인할 수 있습니다.

![Untitled](Untitled%20485.png)

### post 요청 보내기

post 요청은 payload 가 필요합니다.

requests 모듈에서는 payload 를 data 라고 부릅니다.

form 에 아이디와 패스워드를 적으면, http request 의 payload 에 username : babo / password : babo1234 가 담겨서 전송됩니다.

![Untitled](Untitled%20486.png)

아래는 위의 브라우저와 동일한 기능을 하는 코드입니다.

http request method 는 post 로 해서 요청을 전송하고, 받은 response 를 출력합니다.

```python
import requests

url = 'http://localhost:8000/index.php'
data = {'username': 'babo', 'password': 'babo1234'}

response = requests.post(url, data=data)

print(response.text)
```

![Untitled](Untitled%20487.png)

babo 유저의 개인페이지 php 파일이 도착합니다.

### post 요청 보낼때 저장된 쿠키 얻기

- requests.get() 과 requests.post() 는 response 의 header 의 status code 가 302 즉 리다이렉트이면, 자동으로 모든 리다이렉트를 수행하고 마지막 response 를 저장하도록 되어있습니다.
- 고양이 웹에서, set-cookie 헤더는 첫 response 의 header에 있으므로, 자동 리다이렉트를 꺼야합니다.
- allow_redirects = False 로 설정하면 됩니다.

response.cookies 에는 set-cookie 헤더에 있는 쿠키값을 배열로 저장합니다.

for in 문을 이용하여 이를 읽어서 출력할 수 있습니다.

```python
import requests

url = 'http://localhost:8000/index.php'
data = {'username': 'babo', 'password': 'babo1234'}

response = requests.post(url, data=data, allow_redirects=False)

cookies = response.cookies

for cookie in cookies:
    print(f"{cookie.name}: {cookie.value}")

```

쿠키가 담긴 배열

![Untitled](Untitled%20488.png)

쿠키가 담긴 배열을 읽어서 출력

![Untitled](Untitled%20489.png)

또한, response.status_code 를 이용하여 리다이렉트의 status code 인 302 가 헤더에 있음도 알 수 있습니다.

```python
import requests

url = 'http://localhost:8000/index.php'
data = {'username': 'babo', 'password': 'babo1234'}

response = requests.post(url, data=data, allow_redirects=False)

print(response.headers)
print(response.status_code)
```

![Untitled](Untitled%20490.png)

### 쿠키를 포함해서 request 보내기

cookies 에 쿠키값을 대괄호로 둘러싼 후, 콜론(:)으로 구분해서 넣으면 됩니다.

마찬가지로 allow_redirects=False 로 해줍니다.

쿠키값이 틀리면 리다이렉트를 요청하는 response 가 옵니다.

맞으면 리다이렉트되지 않고, babo 의 개인페이지가 response.text 에 저장됩니다.

```python
url = 'http://localhost:8000/page-babo.php'

cookies = {
    'user':'babo_bs'
}

response = requests.get(url, cookies=cookies,allow_redirects=False)

print(response.text)
```

계속