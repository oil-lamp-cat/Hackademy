# 웹해킹 : Cat Homepage

## 고양이 홈페이지, 직접 만들고 직접 해킹하기

<aside>
💡 완성된 코드는 여기에 있으니, 코드가 오류를 일으키면 확인하세요.

</aside>

<aside>
💡 **전재호 버전**

[GitHub - grape942/php_cat_homepage_tutorial](https://github.com/grape942/php_cat_homepage_tutorial)

</aside>

<aside>
💡 **aptheparker (3기) 버전**
(이게 더 코드가 깔끔할지도…ㅎ)

[GitHub - aptheparker/cat-homepage: Web hacking (Broken Access Control & Sql Injection) Practice](https://github.com/aptheparker/cat-homepage)

</aside>

<aside>
💡 **손기민 버전**
(광기의 챕터별 커밋)

[GitHub - KiminSon/cat-homepage](https://github.com/KiminSon/cat-homepage)

</aside>

# 웹과 웹해킹

[웹 해킹에 대하여](%E1%84%8B%E1%85%B0%E1%86%B8%20%E1%84%92%E1%85%A2%E1%84%8F%E1%85%B5%E1%86%BC%E1%84%8B%E1%85%A6%20%E1%84%83%E1%85%A2%E1%84%92%E1%85%A1%E1%84%8B%E1%85%A7%2000a519110749423680950d365b6b722e.md)

[웹 서버 및 홈페이지 취약점 점검 가이드북](%E1%84%8B%E1%85%B0%E1%86%B8%20%E1%84%89%E1%85%A5%E1%84%87%E1%85%A5%20%E1%84%86%E1%85%B5%E1%86%BE%20%E1%84%92%E1%85%A9%E1%86%B7%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%B5%20%E1%84%8E%E1%85%B1%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%8C%E1%85%A5%E1%86%B7%20%E1%84%8C%E1%85%A5%E1%86%B7%E1%84%80%E1%85%A5%E1%86%B7%20%E1%84%80%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%83%E1%85%B3%E1%84%87%E1%85%AE%E1%86%A8%2002c5c29f84914910a9b7368ae1dfe76e.md)

# 웹을 먼저 만들면서 해킹해보기

[Visual Studio Code 와 Docker 연결](Visual%20Studio%20Code%20%E1%84%8B%E1%85%AA%20Docker%20%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%AF%207c870e78114e4af694c2bdc0994b3d45.md)

[고양이 홈페이지 개요 : 웹이란?](%E1%84%80%E1%85%A9%E1%84%8B%E1%85%A3%E1%86%BC%E1%84%8B%E1%85%B5%20%E1%84%92%E1%85%A9%E1%86%B7%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%B5%20%E1%84%80%E1%85%A2%E1%84%8B%E1%85%AD%20%E1%84%8B%E1%85%B0%E1%86%B8%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A1%E1%86%AB%20f625ff54d0b1485291ae19e52fa9348e.md)

[고양이 홈페이지를 만들자 : php 환경세팅](%E1%84%80%E1%85%A9%E1%84%8B%E1%85%A3%E1%86%BC%E1%84%8B%E1%85%B5%20%E1%84%92%E1%85%A9%E1%86%B7%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%B5%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%8C%E1%85%A1%20php%20%E1%84%92%E1%85%AA%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%E1%84%89%E1%85%A6%E1%84%90%E1%85%B5%E1%86%BC%202bbeb17467e94e1396d10327929ed852.md)

### 1_html_web 만들기

[1_html_web-1 : 태그](1_html_web-1%20%E1%84%90%E1%85%A2%E1%84%80%E1%85%B3%20b5fa4949b184466987a62af4294aa7a8.md)

[1_html_web-2  : 로그인 화면 만들기](1_html_web-2%20%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5%20c932287573974a0ca1c1ab2b0a73bbc5.md)

[1_html_web-3: style 태그로 꾸미기](1_html_web-3%20style%20%E1%84%90%E1%85%A2%E1%84%80%E1%85%B3%E1%84%85%E1%85%A9%20%E1%84%81%E1%85%AE%E1%84%86%E1%85%B5%E1%84%80%E1%85%B5%205cce80ec263f475ea379630c5fedf59f.md)

### 2_login 만들기

[2-1_endpoint_login : 개인 페이지 엔드포인트 만들기](2-1_endpoint_login%20%E1%84%80%E1%85%A2%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%B5%20%E1%84%8B%E1%85%A6%E1%86%AB%E1%84%83%E1%85%B3%E1%84%91%E1%85%A9%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%90%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%204b9d637b5f7842b4ae0313d09f6237ea.md)

[2-2 개념 : php 와 url query](2-2%20%E1%84%80%E1%85%A2%E1%84%82%E1%85%A7%E1%86%B7%20php%20%E1%84%8B%E1%85%AA%20url%20query%2041edd2efe8a8421f9451054df52f755d.md)

### 3_form_login 만들기

[3-1_form_login : 폼 로그인 만들기](3-1_form_login%20%E1%84%91%E1%85%A9%E1%86%B7%20%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5%20fe55a602272045d29456477eae411fcb.md)

[3-2_form_login Hacking : Broken Access Control Vulnerability](3-2_form_login%20Hacking%20Broken%20Access%20Control%20Vulne%20c60be71038334751b334f692138c331d.md)

### 4_Cookie

[4-1_Cookie : Broken Access Control Mitigation](4-1_Cookie%20Broken%20Access%20Control%20Mitigation%20a8be07c4c98c46e590da326217a345c2.md)

[4-2_cookie_login : 쿠키 로그인](4-2_cookie_login%20%E1%84%8F%E1%85%AE%E1%84%8F%E1%85%B5%20%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%86%AB%2012288f8e366d420884def623641e5949.md)

[4-3_cookie_login_Hacking : Client-side Cookie Poisoning](4-3_cookie_login_Hacking%20Client-side%20Cookie%20Poison%20c3816889ae8040e88446d91e0b9a3e05.md)

### 5_Cookie_Auth

[5-1_cookie_auth : grape 와 babo 쿠키 인증 시스템](5-1_cookie_auth%20grape%20%E1%84%8B%E1%85%AA%20babo%20%E1%84%8F%E1%85%AE%E1%84%8F%E1%85%B5%20%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%B3%E1%86%BC%20%E1%84%89%E1%85%B5%E1%84%89%E1%85%B3%E1%84%90%E1%85%A6%E1%86%B7%2037b57330eab74291a7627fe04c92a3ae.md)

[5-2_cookie_auth_Hacking : 추측하기 쉬운 쿠키값으로 인한 취약점](5-2_cookie_auth_Hacking%20%E1%84%8E%E1%85%AE%E1%84%8E%E1%85%B3%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20%E1%84%89%E1%85%B1%E1%84%8B%E1%85%AE%E1%86%AB%20%E1%84%8F%E1%85%AE%E1%84%8F%E1%85%B5%E1%84%80%E1%85%A1%E1%86%B9%E1%84%8B%E1%85%B3%E1%84%85%209006409b5f21451abe1aa3a9a9be4c0a.md)

[풀어봅시다 : DreamHack : Cookie](%E1%84%91%E1%85%AE%E1%86%AF%E1%84%8B%E1%85%A5%E1%84%87%E1%85%A9%E1%86%B8%E1%84%89%E1%85%B5%E1%84%83%E1%85%A1%20DreamHack%20Cookie%201584f9e449bf4804bc47299cb6bd85ba.md)

[5-3_cookie_auth_Mitigation : 쿠키값을 추측하기 어렵게 만들기](5-3_cookie_auth_Mitigation%20%E1%84%8F%E1%85%AE%E1%84%8F%E1%85%B5%E1%84%80%E1%85%A1%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%AF%20%E1%84%8E%E1%85%AE%E1%84%8E%E1%85%B3%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20%E1%84%8B%E1%85%A5%208548adbe277944ffae9f2f82c9768de6.md)

### 6_Python_Request

[6-1_cookie_auth : Http Request](6-1_cookie_auth%20Http%20Request%209c88c253f7e148e1a49c3a4a00f0d95d.md)

[6-2_cookie_auth : requests.py](6-2_cookie_auth%20requests%20py%2017d7a96649ba4ec3bc0b93f8415cc614.md)

[6-3_cookie_auth_Hacking : requests.py 를 이용한 Brute Force Attack(무차별대입공격)](6-3_cookie_auth_Hacking%20requests%20py%20%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB%20B%200429dc317cb4412ea974323a8e6bdb27.md)

[6-4_cookie_auth_Hacking : 버프 스위트(Burp Suite)](6-4_cookie_auth_Hacking%20%E1%84%87%E1%85%A5%E1%84%91%E1%85%B3%20%E1%84%89%E1%85%B3%E1%84%8B%E1%85%B1%E1%84%90%E1%85%B3(Burp%20Suite)%20fbb8e94ac71b4078aa66c28b344be2c5.md)

[Windows Google Chrome 브라우저에 burp suite proxy 달기](Windows%20Google%20Chrome%20%E1%84%87%E1%85%B3%E1%84%85%E1%85%A1%E1%84%8B%E1%85%AE%E1%84%8C%E1%85%A5%E1%84%8B%E1%85%A6%20burp%20suite%20proxy%20%2052b85b8cfc864bc99caf5e9e5acae8c6.md)

### 7_Session

[7-1_Session 개념](7-1_Session%20%E1%84%80%E1%85%A2%E1%84%82%E1%85%A7%E1%86%B7%2070660f0f34eb4d9d8b8cc3a05f7ef2c4.md)

[7-2_Session_login : 세션 로그인](7-2_Session_login%20%E1%84%89%E1%85%A6%E1%84%89%E1%85%A7%E1%86%AB%20%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%86%AB%209f515b86300c4afe9d974d0dd602dbd8.md)

[7-3_Session_login_Hacking : Session Hijaking](7-3_Session_login_Hacking%20Session%20Hijaking%2036b8f8db05fa40f98fbe1ab737822701.md)

### 8_Database

[8-1_database : SQL 이란](8-1_database%20SQL%20%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A1%E1%86%AB%202238ea7100fc468e870d56c55297dc86.md)

[8-2_database : vscode SQLite Viewer](8-2_database%20vscode%20SQLite%20Viewer%208fc3391597e7461e9e5d873082a254b5.md)

[8-3_database : sqlite3-php 실습](8-3_database%20sqlite3-php%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%B3%E1%86%B8%2014d8809bdb82403183d7b12cec80409c.md)

[8-4_database : 고양이 홈페이지의 데이터베이스 만들기](8-4_database%20%E1%84%80%E1%85%A9%E1%84%8B%E1%85%A3%E1%86%BC%E1%84%8B%E1%85%B5%20%E1%84%92%E1%85%A9%E1%86%B7%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%B5%E1%84%8B%E1%85%B4%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%87%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B3%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%20270c5614480242128f31dc2cab82640a.md)

[8-5_database : SQL Injection](8-5_database%20SQL%20Injection%20cbff33e9a41445ee8f16655b5c27b29b.md)

[8-6_database : 입력값 검사와 준비된 쿼리](8-6_database%20%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A7%E1%86%A8%E1%84%80%E1%85%A1%E1%86%B9%20%E1%84%80%E1%85%A5%E1%86%B7%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AA%20%E1%84%8C%E1%85%AE%E1%86%AB%E1%84%87%E1%85%B5%E1%84%83%E1%85%AC%E1%86%AB%20%E1%84%8F%E1%85%AF%E1%84%85%E1%85%B5%2025676dc0ab0e438b8b1156d14ae9f87d.md)

[Google Chrome 브라우저에 burp suite proxy 달기 (1)](Google%20Chrome%20%E1%84%87%E1%85%B3%E1%84%85%E1%85%A1%E1%84%8B%E1%85%AE%E1%84%8C%E1%85%A5%E1%84%8B%E1%85%A6%20burp%20suite%20proxy%20%E1%84%83%E1%85%A1%E1%86%AF%E1%84%80%E1%85%B5%20(1%20850865b8e7624003aa98d5e91b79cd51.md)