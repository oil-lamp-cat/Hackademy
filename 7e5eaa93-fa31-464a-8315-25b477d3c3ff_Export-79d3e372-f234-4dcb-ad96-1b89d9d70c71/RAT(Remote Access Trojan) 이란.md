# RAT(Remote Access Trojan) 이란?

<aside>
💡 author : 전재호(agamtt) 2023-09-23

</aside>

<aside>
💡 100% 파이썬으로 개발된 WIndows 원격 제어 트로이 목마인 QuokkaTheRAT 을 똑같이 따라 코딩해 보면서 트로이 목마의 원리를 학습해봅시다.

</aside>

# 트로이목마

![Untitled](Untitled%20567.png)

**트로이목마(Trojan)** 는 다른 컴퓨터에서 몰래 실행되면서, 악의적인 행동을 하는 컴퓨터 프로그램을 말합니다.

그리스 로마 신화에 등장하는 “트로이 목마”에서 따온 것으로, 트로이 전쟁 때, 튼튼한 트로이 성을 함락시키기 위해 무장한 군인들이 나무로 만든 귀여운 목마 안에 몰래 들어갔다가 성 안에서 나와 성을 함락시켰다는 것에서 유래되었습니다.

트로이목마도, 겉으로는 멀쩡한 프로그램 처럼 보이지만, 사실은 설치된 컴퓨터의 개인정보를 몰래 전송하거나, 컴퓨터를 원격 조종합니다.

# 원격 접속 트로이목마 (Remote Access Trojan, RAT)

트로이목마는 그 기능에 따라 다양하게 분류되는데, RAT(Remote Access Trojan) 은 컴퓨터를 원격으로 조종할 수 있는 기능을 가진 트로이목마입니다. 

![Untitled](Untitled%20568.png)

# 공격자와 피해자 (Attacker and Victim)

보통, 해킹 공격을 하는 경우, 공격자를 “해커”라고 부르기보다는 공격자(Attacker)라고 부릅니다.
피해를 당하는 컴퓨터나 사람을 피해자(Victim) 이라고 부릅니다.

# C&C 서버

C&C 또는 C2 는 Command and Control 의 약자로, RAT 을 이용해 피해자의 컴퓨터에 원격 접속하여 조종하는 공격자의 서버를 말합니다.

# 현실의 RAT

구글에 검색해보면, 세상에는 온갖 RAT 이 개발되어 실제로 해커들에 의해 악용되고 있습니다.

![Untitled](Untitled%20569.png)

![Untitled](Untitled%20570.png)

![Untitled](Untitled%20571.png)

![Untitled](Untitled%20572.png)

# Quokka RAT

아무튼 RAT 은 영어로 “쥐” 랑 철자가 똑같아서, 많은 해커들이 쥐의 종류로 이름을 짓는 경우가 많습니다.

QuokkaTheRAT 은 1년전쯤 제가 재미로 만든 해킹 프로그램으로, 쥐 종류가 뭐가 있을까 찾아보다 보니 그때 당시 쿼카가 유행이라 그렇게 지었습니다(근데 알고보니 캥거루에 더 가깝다더군요)

![귀여운 쿼카의 모습](Untitled%20573.png)

귀여운 쿼카의 모습

아주 기본적인 기능만을 가진 Quokka RAT 를 똑같이 개발해보면서, 네트워크 지식과 바이러스 제작을 배워봅시다.

[https://www.youtube.com/watch?v=03S63IpsXjI](https://www.youtube.com/watch?v=03S63IpsXjI)

계속