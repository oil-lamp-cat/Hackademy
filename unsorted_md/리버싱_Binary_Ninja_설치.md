# 리버싱 : Binary Ninja 설치

# 바이너리 실행파일 다운로드 받기

gcc 로 컴파일한 grapple_storry_2 를 guest 에서 host 로 다운로드 받습니다.

여기서,

guest : docker 로 생성한 ubuntu linux 가 설치된 가상머신

host : 내 노트북 또는 데스크톱 컴퓨터(Windows 또는 MacOS 또는 Linux 가 설치된) 입니다

![image.png](image%2026.png)

host 로 다운로드 받은 파일은 host 에서 실행되지 않을 수도 있습니다.

guest 인 Ubuntu Linux 에서 실행되도록 컴파일된 바이너리이므로, Host OS 가 Linux 가 아니면 실행되지 않습니다.

- 대부분 이 튜토리얼을 진행하고 있는 분들은 Windows 또는 MacOS 를 사용할 것이므로, 실행되지 않습니다.

![image.png](image%2027.png)

그러나 **실행할 수는 없지만, 내용을 읽어서 확인하거나 수정할 수는 있습니다.**

# Binary Ninja 설치

아래에 접속해서, 본인 환경에 맞는 것을 설치합니다.

[https://binary.ninja/](https://binary.ninja/)

![image.png](image%2028.png)

![image.png](image%2029.png)

# Binary Ninja 실행

Start 를 눌러줍니다

![image.png](image%2030.png)

![image.png](image%2031.png)

그리고 다운로드 받은 바이너리를 열면 아래와 같이 열립니다

![image.png](image%2032.png)

계속…