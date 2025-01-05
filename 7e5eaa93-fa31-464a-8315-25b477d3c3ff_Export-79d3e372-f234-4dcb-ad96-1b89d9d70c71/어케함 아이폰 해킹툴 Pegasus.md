# 어케함? 아이폰 해킹툴 Pegasus

애플은 아이폰은 매우 보안이 뛰어나다고 오랫동안 깝쳐 왔습니다.

하지만 신문에 대문짝만하게 나오게 해킹을 당해버렸습니다. 그것도 원격으로 해킹을 당하고 말았죠 꼴이 좋습니다.

2022년 쯤, 이스라엘 해킹팀 NSO Group 이 아이폰을 해킹해서 인권 운동가와 정치인들의 아이폰을 도청하다가 걸렸습니다.

악성앱을 설치하는 방식이 아니라 가만히 있어도 해킹할 수 있는 “제로클릭공격” 이였다고 하는데요 아이폰 사용자가 아무 짓도 안해도, 인터넷에 연결되어있으면 해킹 당할 수 있습니다.

![Untitled](Untitled%20370.png)

![Untitled](Untitled%20371.png)

[보안 자랑했던 아이폰, 이스라엘산 스파이웨어에 해킹 / 연합뉴스TV (YonhapnewsTV)](https://www.youtube.com/watch?v=fKR8r7QUb80)

[이스라엘 스파이웨어 페가수스에 '아이폰'도 뚫렸다 - 머니투데이](https://news.mt.co.kr/mtview.php?no=2021072011591992446)

아래는 구글의 보안전문가들이 분석한 Pegasus 의 작동 원리입니다.

[A deep dive into an NSO zero-click iMessage exploit: Remote Code Execution](https://googleprojectzero.blogspot.com/2021/12/a-deep-dive-into-nso-zero-click.html)

이스라엘 해킹업체는 아이폰에 설치된 iMessage(아이메세지) 라는 앱의 취약점을 이용했습니다.

아이메세지에서 JBIG 이라는 사진 포맷을 처리하는 코드의 메모리 취약점을 이용해서, 아이메세지로 악성코드가 심어진 사진파일을 보내서 아이폰에서 임의코드를 실행합니다.

![Untitled](Untitled%20372.png)

![Untitled](Untitled%20373.png)

![Untitled](Untitled%20374.png)

![Untitled](Untitled%20375.png)

사진을 처리하기 위해 할당된 메모리에서 취약점이 발생해서, 아이메세지가 악성코드를 실행합니다.

![Untitled](Untitled%20376.png)

이 취약점은 애플이 부랴부랴 패치를 했습니다. (그리고 이스라엘 업체를 고소했습니다.)

[애플, '페가수스' 만든 이스라엘 업체 고소.."아이폰 접근 금지" 요구](https://www.etnews.com/20211124000121)

# 메모리 취약점

[https://www.cvedetails.com/product/15556/Apple-Iphone-Os.html?vendor_id=49](https://www.cvedetails.com/product/15556/Apple-Iphone-Os.html?vendor_id=49)

실제로 애플의 제품들에 대해서 많은 취약점이 보고 되어있습니다.

![image.png](image%2063.png)

![image.png](image%2064.png)

# PhotoDot

도대체 이게 어떻게 가능한 것인지, 직접 해봅시다.

근데 애플은 자기들을 해킹하면 가차없이 고소를 하는데요

그래서 아이폰에서 실습을 할 수는 없으니, 유사한 상황을 가진 앱을 준비했습니다.

아이폰에 아이메세지로 사진을 볼 수 있는 것 처럼, PhotoDot 은 사진 파일을 여는 것을 모사해서 도트 파일을 열어서 이미지를 보여줍니다.

PhotoDot 의 이미지 처리 시스템을 해킹하면서, 메모리 취약점에 대해 간략히 배워봅시다.

![Untitled](Untitled%201.png)

계속.