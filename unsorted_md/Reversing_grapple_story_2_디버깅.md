# Reversing : grapple_story_2 디버깅

<aside>
💡 author : agamtt(전재호) 2024-01-26

</aside>

# grapple_story_2

우리가 gcc 로 컴파일해서 생성한 실행파일을 이용해서, 디버깅해보겠습니다.

![Untitled](Untitled%20316.png)

실행파일을 gdb 로 실행합니다.

```bash
gdb ./grapple_story_2
```

![Untitled](Untitled%20317.png)

```bash
gdb> b main # main 함수에 breakpoint 를 설정한다.
gdb> i b # breakpoint 가 번호와 함께 출력된다.
gdb> del 1 # main 에 설정한 breakpoint 가 삭제된다. 
gdb> i b # 삭제되었는지 확인해본다.
```

![Untitled](Untitled%20318.png)

이제 main 에 다시 bp 를 설정하고, run 합니다.

```bash
gdb> b main
gdb> r
```

![Untitled](Untitled%20319.png)

그러면 프로그램이 실행됩니다.

![Untitled](Untitled%20320.png)

ni 를 입력하고 엔터를 칠 때마다, 코드가 한줄 한줄 실행됩니다.

```bash
gdb> ni
```

![Untitled](Untitled%20321.png)

이제 ni 를 입력할때마다, 한줄 한줄 실행됩니다.

# 행동을 선택하세요

ni 를 하다보면, “행동을 선택하세요” 부분이 나옵니다.

두개의 행동 중에, “공격” 부분을 분석해봅시다.

0 을 입력하고 엔터를 칩니다.

![Untitled](Untitled%20330.png)

여기서 작동을 예측해봅시다.

- 드래곤에게 플레이어가 공격을 한다는 것은, “드래곤의 체력” 변수에서 “플레이어의 공격력” 을 뺄셈하는 것을 말합니다.
- 즉, 기계어 명령어 중, “드래곤의 체력” 에서 “플레이어의 공격력” 을 빼는 부분이 무조건 있을 수 밖에 없습니다.

코드에서는 이 부분입니다.

우리는 코드가 없고, 실행파일 바이너리만 있다고 가정하고 있으므로, 디버거를 이용하여 이 부분을 찾아봅시다.

![Untitled](Untitled%20331.png)

계속 ni 를 하다보면, main+258 에서 이런 부분을 찾을 수 있습니다.

- 뭔진 모르겠는데 스택의 rbp-0x14 에서 eax 를 뺍니다.
- 예상했던대로 빼는 연산 (sub) 를 하는 곳이 존재합니다.

![Untitled](Untitled%20332.png)

이 부분입니다.

```nasm
sub dword ptr [rbp-0x14], eax
```

- [rbp-0x14] 는, “스택메모리가 시작되는 부분으로 부터 0x14 만큼 떨어진 곳” 을 의미합니다.
- dword ptr 는 해당 부분으로 부터 두개의 WORD 만큼(double word) 가져오세요, 참조하세요(ptr) 라는 뜻입니다. word 가 2byte 니까 double word 는 4byte 입니다. 즉, 아래만큼 복사해오라는 말이지요.
    
    ![Untitled](Untitled%20333.png)
    
- rbp-0x14 부터 4칸의 메모리에 있는 값에서, eax 에 저장된 값을 뺄셈하는 명령입니다.
- 즉, dword ptr [rbp-0x14] 는 드래곤의 체력이고, eax 는 플레이어의 공격력입니다.

REGISTERS 를 확인해보면,

- eax 와 rax 는 똑같습니다. (32비트, 64비트 구분입니다.)
- 빼기를 하는 RAX 에 0x6, 즉 플레이어의 공격력이 저장되어있습니다.

![Untitled](Untitled%20334.png)

그럼 RAX 에 언제 0x6 이 저장되는지, 다시 run 해 봅시다.

```nasm
gdb> r
```

또 공격을 선택(0을 입력) 하고, ni 를 해가다보면,

RAX 에 플레이어의 공격력인 0x6 이 저장되는 부분이 나옵니다.

- main+255 : mov eax, dword ptr [rbp - 0x10] 를 실행하기 직전에는 RAX 에 0x35 가 저장되어 있습니다.
- main+255 를 실행하는 순간, RAX 가 0x6 으로 바뀝니다.
- 즉, main+255 가 플레이어의 공격력을 설정하는 부분입니다.

![Untitled](Untitled%20335.png)

![Untitled](Untitled%20336.png)

즉,

- 스택메모리에서, [rbp - 0x10] 에서 dword ptr 만큼 (4byte) 이 플레이어의 공격력이 저장되어있는 곳이고,  [rbp - 0x14] 에서 dword ptr 만큼(4byte) 이 드래곤의 체력이 저장되어있는 곳입니다.
- eax 를 거쳐서 드래곤의 체력에서 플레이어의 공격력이 뺄셈됩니다.

그렇다면,  dword ptr [rbp - 0x14] 는 언제 설정될까요? 프로그램을 다시 run 해보면,

```nasm
gdb> r
```

 

main+27 ~ main+55 에서 해당 스택메모리에 mov 로 값을 복사하는 부분이 있습니다.

![Untitled](Untitled%20337.png)

이 부분은 코드에서 체력과 공격력을 설정하는 부분이 번역된 부분이라는 것을 알 수 있습니다.

![Untitled](Untitled%20338.png)

# 정리

분석한 결과를 정리하면,

- 드래곤의 체력을 0으로 만들어야 게임을 클리어 할 수 있습니다.
- **드래곤의 체력**에서 **플레이어의 공격력** 을 빼는 부분을 분석했습니다.
- dword ptr [rbp - 0x10] 에 **플레이어의 공격력**이 저장되어 있습니다.
- dword ptr [rbp - 0x14] 에 **드래곤의 체력**이 저장되어 있습니다.

# 어떻게 해킹할까

그럼 두가지 중 하나를 하면 게임을 클리어 할 수 있을 것 같습니다.

- 드래곤의 체력을 작게 바꾼다.
- 플레이어의 공격력을 크게 바꾼다.

계속