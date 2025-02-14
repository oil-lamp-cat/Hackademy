# 6-4_cookie_auth_Hacking : 버프 스위트(Burp Suite)

<aside>
💡 author : agamtt(전재호) 2024-01-26
contributor : 손기민(KiminSon) 2024-04-08

</aside>

# 웹 디버거, Burp Suite

개발자 콘솔로 해킹하는 것은 좋지만, 불편한 점도 많습니다.

웹 디버거를 이용하면, 해킹을 위한 다양한 편의기능을 제공합니다.

# Windows 에서 설치하기

[버프 스위트(Burp Suite) 설치 방법](https://securityspecialist.tistory.com/113)

# MacOS 에서 설치하기

[macOS 환경에서 Burp Suite 설치 및 설정하기](https://hooneee.tistory.com/373)

# Cat Homepage Burp!

버프 스위트를 실행해서 고양이 홈페이지를 디버깅 해봅시다.

![Untitled](Untitled%20509.png)

# Proxy

Proxy 탭 안의 Intercept 탭을 들어가서 Open Browser 를 누릅니다.

![Untitled](Untitled%20510.png)

![Untitled](Untitled%20511.png)

![Untitled](Untitled%20512.png)

그러면 Burp Suite 와 연결된 특수하개 개조된 크롬 브라우저가 열립니다.

- 이 브라우저로 웹사이트에 접속하면 오고 가는 패킷이 전부 Burp Suite 에 기록됩니다.

![Untitled](Untitled%20513.png)

고양이 홈페이지에 접속해봅시다.

![Untitled](Untitled%20514.png)

이 특수한 크롬 브라우저로 웹을 사용하면, 이 브라우저를 거친 모든 HTTP 통신이 Burp Suite 에 기록됩니다.

Proxy 탭의 HTTP history 에 들어가서 Request 와 Response 를 조회할 수 있습니다.

![Untitled](Untitled%20515.png)

# Intercept / Request 변조

python의 request 모듈을 이용해서 HTTP Request 를 보낼 수 있었습니다.

웹브라우저의 개발자 콘솔을 이용하여 Request 를 확인하고, 이에 맞게 포맷을 작성해서 보냈습니다.

Burp Suite 를 이용하면 더 편하게 변조된 Request 를 보낼 수 있습니다.

proxy/intercept 탭에 Intercept On 버튼을 클릭합니다.

 

![Untitled](Untitled%20516.png)

- 이제 Burp Suite 의 브라우저는 곧바로 HTTP Request 를 보내지 않고, 보내기전에 “멈춥니다”
- Burp Suite 에서 내용을 내맘대로 바꿔서 Request 를 보낼 수 있습니다.
    - 이것을 Request 변조(Request Forgery) 라고 부릅니다.

Intercept mode 가 켜진 상태에서, Burp Suite 브라우저에서 고양이 홈페이지에 이상한 아이디 비번으로 로그인해봅시다.

![Untitled](Untitled%20517.png)

그러면 바로 POST Request 를 보내는게 아니라, Burp Suite 에 보낼 Request 가 저장됩니다.

![Untitled](Untitled%20518.png)

# Repeater

이 신호를 변조해봅시다.

Ctrl + R 을 누르거나, 우클릭 후 Send to Repeater 를 클릭합니다.

![Untitled](Untitled%20519.png)

그러면 Proxy 탭에서 Repeater 탭으로 저장된 Request 가 이동합니다.

Reapeater 탭으로 이동해서 확인합니다.

![Untitled](Untitled%20520.png)

Send 를 누르면 Request 가 전송됩니다.

우측에서 서버가 보낸 Response 를 확인할 수 있습니다.

![Untitled](Untitled%20521.png)

Render 탭에 들어가면 Response 의 Html 을 렌더링해서 보여줍니다.

![Untitled](Untitled%20522.png)

Request 탭에서는 보내기 전에 Request 를 수정할 수 있습니다.

Request 에 포함된 값을 수정하면, 수정된 것 보냈을 때 어떤 결과가 나오는지 바로 비교해 볼 수 있습니다.

![Untitled](Untitled%20523.png)

![Untitled](Untitled%20524.png)

이것은 Python request 모듈로 아래와 같이 코딩해서 실행하는 것과 동일하게 작동합니다.

```bash
import requests

url = 'http://localhost:8000/index.php'
data = {'username': 'babo', 'password': 'babo1234'}

response = requests.post(url, data=data, allow_redirects=False)

print(response.headers)
print(response.status_code)
```

# Burp Suite 와 웹해킹

Burp Suite 말고 Zed Proxy 나 Fiddler 같은 툴도 씁니다만

Burp Suite 가 해킹 및 보안업계 표준 툴이나 다름이 없기 때문에, 익혀두는 것이 좋습니다.

성능도 제일 좋고 디자인도 예쁩니다.

계속