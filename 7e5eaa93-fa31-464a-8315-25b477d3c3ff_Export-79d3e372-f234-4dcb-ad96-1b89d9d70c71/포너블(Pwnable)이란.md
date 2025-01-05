# 포너블(Pwnable)이란

<aside>
🧑🏻‍💻 author : 전재호(agamtt) 2024-03-12

</aside>

**포너블(Pwnable)**은 운영체제, 소프트웨어, 하드웨어의 시스템에 내제된 보안 취약점을 해킹하는 것을 말합니다.  **시스템해킹**이라고도 불립니다.

이 시스템 내가 차지했다(own) 의 오타인 pwn 에서 유래되었다고 하네요.

![Untitled](Untitled%20364.png)

우리가 핸드폰에서 앱을 실행하건, python 이나 JAVA 코드를 실행하던, 결국은 컴퓨터에서 작동합니다.

이런 시스템 소프트웨어들은 전통적으로는 C언어나 C++언어로 개발됩니다. (요즘은 새로운 언어인 Rust 를 쓴다 어쩐다 하고 있는 상태임)

# Pwn!

포너블 기술을 이용해서 할 수 있는 일들은 무궁무진 합니다.

예를 들면,

### 취약점을 이용한 안드로이드 스마트폰 루팅

- 안드로이드 스마트폰의 루트 권한은 기본적으로 사용자가 사용할 수 없습니다. LPE(Local Privilege Escalation) 이라는 종류의 취약점을 이용하여 root 를 얻는 방식으로 루팅하는 경우가 많은데, pwnable 기술이 사용됩니다.

[https://www.youtube.com/watch?v=00qq4-P3RL0](https://www.youtube.com/watch?v=00qq4-P3RL0)

[https://www.youtube.com/shorts/14UcNcW4r0Q?si=VHCEgdJwYgzLm-Y9](https://www.youtube.com/shorts/14UcNcW4r0Q?si=VHCEgdJwYgzLm-Y9)

### 취약점을 이용한 아이폰 탈옥

- 아이폰은 사용자 맘대로 앱을 설치하거나 포트를 열 수 없습니다. 앱스토어에 있는 앱만 설치할 수 있고, 설정앱에 없는 기기 설정을 변경할 수 없습니다.
- 아이폰 탈옥툴들은 pwnable 기술을 이용하여 아이폰 메모리를 해킹하고, LPE 로 아이폰의 root 권한을 얻는 방식으로 아이폰의 보안을 해제합니다
    
    ![Untitled](Untitled%20365.png)
    

[https://www.youtube.com/shorts/8fMTSZWXxOw?si=Fie-Bc_UBuk6u8OF](https://www.youtube.com/shorts/8fMTSZWXxOw?si=Fie-Bc_UBuk6u8OF)

[https://www.youtube.com/shorts/WIwnAcV3G48?si=vWptSCSB0BLvU1ho](https://www.youtube.com/shorts/WIwnAcV3G48?si=vWptSCSB0BLvU1ho)

- 인터넷 장비 (아이피 카메라, 공유기 등) 의 펌웨어를 해킹한 후 공유기에 연결된 스마트폰, 데스크톱 등에 접근하기
    - 대부분의 네트워크 장비는 임베디드 리눅스를 커스텀한 펌웨어를 사용합니다. 공유기의 특성상 외부와 인터넷으로 연결되므로, 해커가 원격에서 해킹할 수 있는 경우가 있습니다. ([https://app.opencve.io/cve/?&vendor=iptime](https://app.opencve.io/cve/?&vendor=iptime))
    - ([https://krcert.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000302&searchWrd=iptime&menuNo=205023&pageIndex=1&categoryCode=&nttId=36364](https://krcert.or.kr/kr/bbs/view.do?searchCnd=1&bbsId=B0000302&searchWrd=iptime&menuNo=205023&pageIndex=1&categoryCode=&nttId=36364))

### 시스템 소프트웨어 해킹

Java, Python, Javascript 같은 프로그래밍 언어로 코딩을 할때,

앱 개발자나 웹 개발자가 컴퓨터 메모리 관련 코드를 코딩하지 않아도, 시스템 소프트웨어가 우리 대신 메모리를 제어해줍니다.

코드가 실행될때 메모리를 제어하고 코드를 실행시켜주는 또다른 프로그램을 런타임(Runtime) 이라고 부릅니다.

이러한 런타임에 취약점이 있는 경우, 코드가 맘대로 실행될 수 있습니다.

### 운영체제 커널 해킹

운영체제의 기능을 사용할때, 응용프로그램이 “시스템콜” 이라는 것을 사용해야합니다.

“시스템콜” 의 데이터는 운영체제의 커널에서 작동하므로 커널 영역의 메모리가 직접 손상될 수 있습니다. 해커들은 특별하게 제작된 코드를 이용해서 커널을 해킹해서 루트를 얻거나 다양한 악성 행위를 할 수 있습니다

### 그 외 장비 해킹 - 게임기 해킹

닌텐도 스위치에 공짜 게임을 깔 수 있게 해주는 “커스텀 펌웨어” 의 원리도 Pwnable 입니다.

![Untitled](Untitled%20366.png)

[또 칩 단계 취약점? 닌텐도 스위치 제품 전부 위험](https://www.boannews.com/media/view.asp?idx=68747)

![Untitled](Untitled%20367.png)

![Untitled](Untitled%20368.png)

## RCE(Remote Code Execution)

컴퓨터의 **외부 입력**이 메모리 버그를 일으키는 경우, 잘 하면 원격에서 메모리를 손상시켜서 pwnable 계열의 취약점을 악용할 수도 있습니다.

2021년에 발견된 아이폰 해킹툴 “페가수스” 는 Pwnable 기법인 정수오버플로우 취약점을 이용합니다.

- 외부에서 전화번호나 icloud 계정으로 아이메세지에 특수하게 제작된 이미지를 전송합니다.
- iMessage 앱의 CoreGraphics API 를 통해 아이폰의 메모리를 손상시킵니다.
- 이를 통해 임의 코드를 실행할 수 있게 되고, 악성 루트킷을 설치합니다.
- 해커가 원격에서 인터넷 네트워크를 통해 전화 도청, 저장된 메세지, 사진, 그 외 모든 스마트폰를 거쳐가는 모든 통신, 스마트폰에 저장된 모든 파일을 읽거나 수정 가능합니다

[이스라엘 해킹도구 페가수스, 최신 아이폰 보안도 뚫었다](https://www.hani.co.kr/arti/international/international_general/1009034.html)

[Analyzing Pegasus Spyware’s Zero-Click iPhone Exploit ForcedEntry](https://www.trendmicro.com/ru_ru/research/21/i/analyzing-pegasus-spywares-zero-click-iphone-exploit-forcedentry.html)

![Untitled](Untitled%20369.png)

### 브라우저 해킹

브라우저는 웹서버에서 html, javascript 등을 다운로드 받아서 실행시킵니다.

해커가 악의적인 사이트를 제작한 후, 그 안에 특별하게 제작된 악성코드를 넣으면 해당 사이트에 접속하는 컴퓨터의 브라우저 안의 엔진에서 코드가 작동합니다.

이때, 메모리 취약점이 발생하면 브라우저 안에서 악성코드가 실행되거나, **더욱 심각한 경우, 브라우저를 탈출해서 컴퓨터에 악성코드가 실행되도록 할 수 있습니다.**

[https://www.youtube.com/watch?v=3ogyS4KOlXc](https://www.youtube.com/watch?v=3ogyS4KOlXc)

[https://www.youtube.com/watch?v=63MKVqdEJ6k](https://www.youtube.com/watch?v=63MKVqdEJ6k)

![image.png](image%2062.png)

# 메모리 손상 취약점

포너블 기법은 주로, 메모리 손상 취약점 (Memory Corruption) 을 겨냥합니다

컴퓨터 메모리에 대해 알아보고, 직접 해킹해봅시다.

계속