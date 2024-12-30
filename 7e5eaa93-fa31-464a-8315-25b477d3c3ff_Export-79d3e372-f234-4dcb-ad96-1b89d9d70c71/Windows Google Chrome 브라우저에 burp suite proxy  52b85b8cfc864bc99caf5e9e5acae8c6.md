# Windows Google Chrome 브라우저에 burp suite proxy 달기

<aside>
💡

Windows 11 기준으로 작성되었음. 다른 OS 도 거의 비슷하긴한데,, 메뉴얼을 쓰기 귀찮으므로 필요한 사람은 댓글을 달 것. 
→ 본인이 메뉴얼을 써서 나한테 줘도됨 그럼 감사

</aside>

Google Chrome 설정에서 “인증서 관리” 에 들어간다.

![image.png](image%20187.png)

![image.png](image%20188.png)

[Installing Burp's CA certificate](https://portswigger.net/burp/documentation/desktop/external-browser-config/certificate)

![image.png](image%20189.png)

![image.png](image%20190.png)

![image.png](image%20191.png)

![image.png](image%20192.png)

![image.png](image%20193.png)

![image.png](image%20194.png)

![image.png](image%20195.png)

![image.png](image%20196.png)

![image.png](image%20197.png)

![image.png](image%20198.png)

![image.png](image%20199.png)

![image.png](image%20200.png)

프록시를 사용하면, chrome 브라우저의 모든 통신이 burp suite 를 거쳐간다.

그래서 프록시가 켜져있는 상태에서 burp suite 를 끄면 chrome 의 인터넷을 사용할 수 없다!

프록시를 꺼야 다시 사용할 수 있다.

끌때는 다시 “프록시 서버 사용” 을 끄면 된다.

![image.png](image%20201.png)