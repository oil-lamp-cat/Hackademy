# Reversing : 이진수, 16진수

<aside>
💡 author : agamtt(전재호) 2024-01-26

</aside>

# 진법

십진법, 이진법, 십육진법에 대해 알아야 합니다.

- 아래 표가 익숙해질때까지 암기해야합니다.
- 구구단을 모르면, 미적분을 배울 수 없습니다.
- 구구단을 외워야하는 것처럼, 컴퓨터의 진법을 외우세요.

```
1 bit (이진수 1개)
8 bit = 1 byte (이진수 8개)

한개의 16진수 = 1 hex = 0~15, 16개 표현 = 이진수 4개 = 4 bit

1 byte = 2 hex (이진수 8개 = 16진수 2개)

1 word = 4 hex = 2 byte = 16 bit
```

# 1 bit

1 bit 는 한개의 이진수로, 켜짐, 꺼짐을 나타냅니다.

숫자 2개를 표현할 수 있습니다.

![Untitled](Untitled%20291.png)

# 1 byte

1 byte 는 8개의 이진수로, 숫자 256 개를 표현할 수 있습니다.

1 byte 는 8 bit 와 같습니다.

![Untitled](Untitled%20292.png)

# 1 hex

hex 는 hexadecimal 의 약자로, 16진수를 말합니다.

1 hex 는 4 bit 입니다.

# 1 WORD

네 개의 hex 를 붙인 것을 말합니다.

1 WORD 는 16 bit 이며, 2 byte 입니다.

(예외가 있긴 합니다만, 중요하지 않음.)

![Untitled](Untitled%20293.png)

앞으로 이런 것을 보면, BYTE 로 구분된 표현이라고 생각하면 됩니다.

73 은 하나의 BYTE 입니다. 두개의 16진수이고, 8개의 이진수입니다.

![Untitled](Untitled%20294.png)

두 칸은 하나의 WORD 입니다.

# Carry (자릿수 올림)

이진수는 아래와 같은 순서로 숫자를 셉니다

<aside>
💡 0 1 10 11 100 101 …

</aside>

- 0 과 1 두개로 수를 표현합니다.
- 1 이 최대라서 1보다 커지면 자릿수가 올라갑니다.

십진수는 아래와 같은 순서로 숫자를 셉니다

<aside>
💡 0 1 2 3 4 5 6 7 8 9 10 11 12 13 …

</aside>

- 0 1 2 3 4 5 6 7 8 9 열개로 수를 표현합니다.
- 9 가 최대라서 9보다 커지면 자릿수가 올라갑니다.

16진수는 아래와 같은 순서로 숫자를 셉니다

<aside>
💡 0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 …

</aside>

- 0 1 2 3 4 5 6 7 8 9 A B C D E F 열여섯개로 수를 표현합니다.
- F 가 최대여서 F 보다 커지면 자릿수가 올라갑니다.

# 1 byte = 2 hex = 8 bit

- 컴퓨터 세상에서는 8 개의 이진수를 단위로 수를 세기로 약속했습니다.
    - 뭐, 딱히 이유는 없는데, 7 bit 나 9 bit 는 홀수라서 안나누어 떨어져서 짜증나고요
    - 4 bit 는 너무 작고 16 bit 는 너무 큽니다.
    - 8 bit 가 적당합니다.
    - 8 bit 를 편하게 1 byte 라는 단위로 정했습니다.
- 8 개의 이진수는 1 byte 입니다.
- 1 byte 는 2 자리의 hex 로 표현 가능합니다.
    - 1 hex 는 한자리의 16진수입니다.
    - 8 bit 는 00000000 부터 11111111 까지 2^8=256 개의 숫자를 표현합니다
    - 2 hex = 8 bit 입니다. 00(hex) = 00000000(2) , FF(hex) = 11111111(2) 입니다.

# 메모리

- 컴퓨터 메모리에는 1 과 0 으로 데이터가 저장됩니다.
- 이진수로 표기하면 너무 기니까, 1 byte 단위로, hex로 표기합니다.
- 1 byte 는 2개의 hex 니까, 2개의 hex 로 표현됩니다.

![Untitled](Untitled%20295.png)

# 프로그래머 계산기

- 아인슈타인이 아니니까 16진수를 암산하는 것은 힘든 일 입니다.
- 계산기로 하면 됩니다.

Windows 운영체제를 사용하면, 프로그래머 계산기를 기본 프로그램으로 사용할 수 있습니다.

![Untitled](Untitled%20296.png)

예를 들어 18을 십진수로 입력하면,

Hex, Dec, Oct, Bin 으로 각각 무엇인지 알려줍니다.

- Hex 는 16진수, Dec 는 십진수, Bin 은 이진수를 의미합니다.

![Untitled](Untitled%20297.png)

아니면 구글에 Programmer Calc 를 검색하면 많이 나옵니다.

[Programmers   64-bit Calc  | Bitwise Opertors |Bitshift | Bin | Hex |  RoR | xOr | NAND |XNOR and....](https://calc.penjee.com/)

![Untitled](Untitled%20298.png)

아래를 참고하면 좋습니다.

[Hexadecimal - 2 digits](https://www.gcsecs.com/hexadecimal---2-digits.html)

계속