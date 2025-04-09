# 트로이목마 : Quokka RAT

## 악성코드 제작

<aside>
💡 전재호(88sprout@gmail.com) 2023-06-26

</aside>

<aside>
⚠️ **주의** : 악성코드를 악용하여 개인적/법적 문제가 발생하는 경우, 동아리와는 아무 관련이 없으며 개인의 책임임을 고지합니다.

</aside>

<aside>
💡 **완성된 코드 : aptheparker 버전**

[GitHub - aptheparker/grapple-story: Linux Reversing Practice](https://github.com/aptheparker/grapple-story)

</aside>

## 악성코드란

[악성코드, 컴퓨터 바이러스](%E1%84%8B%E1%85%A1%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%8F%E1%85%A9%E1%84%83%E1%85%B3,%20%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%B2%E1%84%90%E1%85%A5%20%E1%84%87%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A5%E1%84%89%E1%85%B3%20061dae50ca7247e4b7cc2c4e7f3866f5.md)

[RAT(Remote Access Trojan) 이란?](RAT(Remote%20Access%20Trojan)%20%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A1%E1%86%AB%2009fe8e33decb41509ef903c7864d229f.md)

## Quokka RAT

[Quokka RAT : 공격자 서버와 희생자 컴퓨터 생성](Quokka%20RAT%20%E1%84%80%E1%85%A9%E1%86%BC%E1%84%80%E1%85%A7%E1%86%A8%E1%84%8C%E1%85%A1%20%E1%84%89%E1%85%A5%E1%84%87%E1%85%A5%E1%84%8B%E1%85%AA%20%E1%84%92%E1%85%B4%E1%84%89%E1%85%A2%E1%86%BC%E1%84%8C%E1%85%A1%20%E1%84%8F%E1%85%A5%E1%86%B7%E1%84%91%E1%85%B2%E1%84%90%E1%85%A5%20%E1%84%89%E1%85%A2%E1%86%BC%E1%84%89%E1%85%A5%E1%86%BC%20e2db71baeeb845c590df192922355844.md)

[Quokka RAT : 쉘커맨드를 파이썬으로 실행하기 - subprocess](Quokka%20RAT%20%E1%84%89%E1%85%B0%E1%86%AF%E1%84%8F%E1%85%A5%E1%84%86%E1%85%A2%E1%86%AB%E1%84%83%E1%85%B3%E1%84%85%E1%85%B3%E1%86%AF%20%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8A%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%B3%E1%84%85%E1%85%A9%20%E1%84%89%E1%85%B5%E1%86%AF%E1%84%92%E1%85%A2%E1%86%BC%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5%20-%20%206d46077d8cc14d3b98c7efa9cc54ede7.md)

[Quokka RAT : 바인드 쉘과 리버스 쉘](Quokka%20RAT%20%E1%84%87%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%83%E1%85%B3%20%E1%84%89%E1%85%B0%E1%86%AF%E1%84%80%E1%85%AA%20%E1%84%85%E1%85%B5%E1%84%87%E1%85%A5%E1%84%89%E1%85%B3%20%E1%84%89%E1%85%B0%E1%86%AF%203f399a9d2c044b34bd0e1ea7fc868352.md)

[Quokka RAT : subprocess 리버스 쉘 만들기](Quokka%20RAT%20subprocess%20%E1%84%85%E1%85%B5%E1%84%87%E1%85%A5%E1%84%89%E1%85%B3%20%E1%84%89%E1%85%B0%E1%86%AF%20%E1%84%86%E1%85%A1%E1%86%AB%E1%84%83%E1%85%B3%E1%86%AF%E1%84%80%E1%85%B5%203dd7fdba02844340bd28adb2eccfd1a7.md)

[Quokka RAT : 페이로드](Quokka%20RAT%20%E1%84%91%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%85%E1%85%A9%E1%84%83%E1%85%B3%203863a544b6cd43d3a395fb02691e3ebe.md)

[Quokka RAT : 정상프로그램인 척 하는 악성프로그램, 트로이목마](Quokka%20RAT%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%89%E1%85%A1%E1%86%BC%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%86%B7%E1%84%8B%E1%85%B5%E1%86%AB%20%E1%84%8E%E1%85%A5%E1%86%A8%20%E1%84%92%E1%85%A1%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%8B%E1%85%A1%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%20b032d6c559e44eb5b2c3fde9114ab06d.md)

[Quokka RAT : 지속성(Persistance)](Quokka%20RAT%20%E1%84%8C%E1%85%B5%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC(Persistance)%200121d8ca0f0b4139a233c0d21add886e.md)

[Quokka RAT : 다른 OS 에서의 리버스쉘](Quokka%20RAT%20%E1%84%83%E1%85%A1%E1%84%85%E1%85%B3%E1%86%AB%20OS%20%E1%84%8B%E1%85%A6%E1%84%89%E1%85%A5%E1%84%8B%E1%85%B4%20%E1%84%85%E1%85%B5%E1%84%87%E1%85%A5%E1%84%89%E1%85%B3%E1%84%89%E1%85%B0%E1%86%AF%207a0b9ac1cb544acb91ef1da992fdbcf1.md)

## Quokka RAT Windows + Embeded Python

<aside>
💡

Windows 데스크톱이 있으면 재미로 해보시길

</aside>

[Quokka RAT : Windows Embeded Python](Quokka%20RAT%20Windows%20Embeded%20Python%20a4f96ffa8c4b42b58c7e1c538539a6a0.md)