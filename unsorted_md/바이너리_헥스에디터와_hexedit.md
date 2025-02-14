# 바이너리, 헥스에디터와 hexedit

<aside>
⚠️ author : 전재호(agamtt) 2024-03-15

</aside>

참고

[PYRASIS.COM: 초보자를 위한 리버스 엔지니어링 상식 - 기계어를 어셈블리로 해석하기](https://pyrasis.com/blog/entry/ReverseEngineeringTranslateMachineCodeToAssembly)

# 어셈블, 디스어셈블

C언어나 파이썬으로 만든 코드가 컴퓨터에서 실행되려면, 기계어로 변환되어야 합니다.

- C 컴파일러인 gcc 는 .c 파일을 기계어로 변환합니다.
- Python 의 실행파일인 python3 는 .py 코드를 한줄 한줄 기계어로 변환합니다.
    - 한줄 한줄 기계어로 변환하여 실행하는 것을 인터프리팅(interpreting) 이라고 부릅니다.

![Untitled](Untitled%20290.png)

- grapple_story_2.c 는 .c 파일로, 고급 프로그래밍 언어인 C언어로 작성된 인간이 읽을 수 있는 코드입니다.
- grapple_story_2 는 gcc 로 컴파일된, 인간이 아니라 컴퓨터가 읽을 수 있는 기계어파일 입니다.

이런 기계어 파일을 이진수로 쓰여있다고 해서 바이너리(Binary) 파일이라고 부릅니다.

# 바이너리 파일

우리가 만든 grapple_story 는 “바이너리 파일(binrary file)” 입니다. bin 이라고 부르기도 합니다.

- 바이너리 파일은 이진수로 되어있어서 인간이 읽기 힘듭니다.
- 컴퓨터는 바이너리만 이해합니다.

실제 바이너리 파일을 보고, 이해해봅시다.

vscode 는 바이너리 파일을 열려고 하면, “이 파일은 바이너리이거나 읽을 수 없는, 내가 모르는 형식이다” 라는 오류를 뱉습니다.

![Untitled](Untitled%20299.png)

![Untitled](Untitled%20300.png)

그러나 그냥 Open Anyway 를 눌러봅시다

그러면, 어떤 방법으로 읽을 것인지 선택하는 창이 뜹니다.

Text Editor 로 열어봅시다.

![Untitled](Untitled%20301.png)

그러면 아래와 같이 뜹니다.

- Text Editor 는 Text 만 해석할 수 있습니다.
- 우리가 입력한, “현재 드래곤의 공격력” 등이 바로 Text 입니다.
- 그 외에는 해석할 수 없어서 빨간색으로 출력됩니다.

![Untitled](Untitled%20302.png)

이런 바이너리 파일을 읽기 위해서는 헥스 에디터(Hex Editor) 라는 뷰어 프로그램이 필요합니다.

vscode 에서도 플러그인으로 지원합니다.

# vscode Hex Editor

플러그인에서 hex 를 검색해서 다운받습니다.

![Untitled](Untitled%20303.png)

이제 grapple_story 를 클릭해서 읽기를 시도한 후, 선택창에서 Hex Editor 를 실행할 수 있습니다.

![Untitled](Untitled%20304.png)

아래의 못생긴 모습이, grapple_story 라는 파일의 실체입니다.

- grapple_story.c 가 컴파일 되면 기계어로 바뀝니다.
- 그 기계어는 이진수입니다.
- 그 이진수를 4자리씩 끊어서 16진수로 표현한 것이 Hex 입니다.
- Hex 를 사람이 읽을 수 있도록 정리해주는 프로그램이 Hex Editor 입니다.

![Untitled](Untitled%20305.png)

# Hex 문자열

우측 화면의 Decoded Text 는, 좌측의 기계어가 Text 일 것이라고 추측한 후, Text 로 번역해놓은 것 니다. 이것은 ASCII 표라는, 이진수와 알파벳을 일대일대응하는 표를 기준으로 해석한 것 입니다.

![Untitled](Untitled%20306.png)

73 74 61 72 74 5F 6D 61 69 6E 가 보입니다.

16진수를 이진수로 변환하면,

0111(7) 0011(3) 0111(7) 0100(4) 0110(6) 0001(1) 0111(7) … 입니다.

![Untitled](Untitled%20307.png)

구글에 ASCII 표 또는 ASCII Table 을 검색하면, 아래와 같은 일대일대응 표를 얻을 수 있습니다.

아스키표에 따르면,

0111(7) 0011(3) : 73 : s

0111(7) 0100(4) : 74 : t

0110(6) 0001(1) : 61 : a

0111(7) 0010(2) : 72 : r

…

![Untitled](Untitled%20308.png)

# 기계어와 어셈블리

컴퓨터가 이해할 수 있는 것은 기계어 뿐이고, 어셈블리어는 기계어를 인간이 알아듣기 편하게 알파벳으로 표현한 것 임을 배웠습니다.

모든 Hex 가 ASCII Text 인 것은 아닙니다.

컴퓨터가 실행할 수 있는 명령어는 ASCII Text 가 아니지만, Hex Editor 는 이것이 ASCII Text 라고 가정하고 Decoded Text 에 번역해놓습니다.

예를 들어, 00001270 열의 48 89 E5 를 봅시다.

![Untitled](Untitled%20309.png)

![Untitled](Untitled%20310.png)

여기서 48 89 E5 는, ASCII Text 가 아니라, **기계어 명령어** 입니다.

이 코드는 ubuntu linux x86 에서 작동하므로, x86 기계어로 작동합니다.

x86 기계어를 구글에서 찾으면,

이런 표가 나옵니다. 컴퓨터 만든 회사에서, 기계어를 표로 정리해놨습니다.

[coder32 edition | X86 Opcode and Instruction Reference 1.12](http://ref.x86asm.net/coder32.html)

이런 웹사이트를 쓰면 표에 대응하는 기계어를 알아서 번역해줍니다.

[Online x86 and x64 Intel Instruction Assembler](https://defuse.ca/online-x86-assembler.htm#disassembly2)

![Untitled](Untitled%20311.png)

48 89 E5 는 기계어 명령어로,

48 : x64 명령어임을 의미

89 : mov [레지스터], [레지스터]

E5 : 1110 0101

11 : 레지스터-레지스터 간 데이터 전송 모드

100 : esp

101 : ebp

입니다.

![Untitled](Untitled%20312.png)

그러나 디버거에는 기계어 번역기능이 포함되어있으므로, 이렇게 직접 표를 보고 기계어를 번역할 필요는 없습니다.

계속