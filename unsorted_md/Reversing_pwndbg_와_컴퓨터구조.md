# Reversing : pwndbg 와 컴퓨터구조

<aside>
💡 author : agamtt(전재호) 2024-01-26

</aside>

# pwndbg 각 부분 설명

pwndbg 는 

- 레지스터에 현재 저장된 값
- 현재 스택메모리에 저장된 값
- 현재 실행중인 기계어

를 나눠서 보여줍니다.

실행할때마다 세개의 창의 상태가 바뀌면서 프로그램의 작동 구조를 디버깅할 수 있습니다.

### REGISTERS : 레지스터에 현재 저장된 값

REGISTERS 란에서는 레지스터에 저장된 값을 볼 수 있습니다.

- RAX, RBX, RCX … 는 모두 레지스터 이름입니다.
- 예를 들어, 현재 RAX 에는 0x35 라는 숫자가 저장되어 있습니다.

![Untitled](Untitled%20326.png)

### STACK : 현재 스택메모리에 저장된 값

STACK 란에는 현재 스택메모리의 상태가 표시됩니다.

![Untitled](Untitled%20327.png)

잘 보면, 스택메모리 영역을 구분하는 레지스터인 rsp 와 rbp 가 표시되어있음을 확인할 수 있습니다.

![Untitled](Untitled%20328.png)

즉, 메모리주소 0x7fffffffe380 부터 0x7fffffffe360 까지가 스택 메모리 영역입니다. 

### DISASM : 현재 실행중인 기계어

코드를 디스어셈블한 후, 현재 실행중인 부분을 초록색 화살표로 표시해줍니다.

- **초록색 코드는 아직 실행되지 않은 코드입니다**
- 초록색 위로는 이미 실행된 코드입니다.

![Untitled](Untitled%20329.png)

계속