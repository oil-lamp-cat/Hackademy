# GDB : photoDot 동적분석

# gdb 로 photoDot 실행파일 열기

그러면 그냥 실행되는게 아니라, 한줄 한줄 멈춰서 실행됩니다.

![image.png](image%20105.png)

![image.png](image%20106.png)

gdb 를 끄고 나가려면 exit 이라는 명령을 치면 됩니다

```bash
pwndbg> exit
```

# r (run)

gdb 로 실행한 프로그램은 실행하기 전에는 실행되지 않고 멈춰서 대기하고 있습니다.

r 이라는 명령어를 입력하면 그제서야 실행됩니다

```bash
pwndbg> r
```

r 을 누르면 얼마던지 프로그램이 계속 재시작 됩니다.

![image.png](image%20107.png)

# b main (breakpoint main)

그냥 r 명령어로 run 을 하게 되면, 우리는 내부 동작이 궁금한데 그냥 일반적으로 실행할 때 처럼 프로그램이 그냥 실행되어버립니다.

b 라는 명령어로, **중단점(breakpoint)**을 설정할 수 있습니다.

breakpoint 가 설정된 상태로 r 을 하면 **그곳에서 멈춥니다.**

b 뒤에는 주소 또는 함수의 이름이 들어가면 됩니다.

main 함수에서 멈춰봅시다.

```bash
pwndbg>b main
pwndbg>r
```

![image.png](image%20108.png)

# i b (info breakpoint), del <num>

만든 breakpoint 는 i b 라는 명령어를 입력하면 볼 수 있습니다

del 로 breakpoint 를 삭제할 수 있습니다.

i b 로 확인한 breakpoint 의 Num 을 del 뒤에 입력하면 됩니다.

![image.png](image%20109.png)

```bash
pwndbg>b main # main 에 breakpoint 가 걸린다.
pwndbg>i b # breakpoint 를 확인해보면 main 에 걸려있다
pwndbg>del 1 # breakpoint 를 지운다.
pwndbg>i b # breakpoint 를 확인해보면 지워져있다
```

## b <주소>

특정 함수 뿐만 아니라, 주소에도 breakpoint 를 걸 수 있습니다.

- hex 를 넣으려면 0x 를 앞에 붙여야함
- 함수 이름과 구별하기 위해서 맨 앞에 * 을 붙여야함
    - 0x40129c 라는 이름을 가진 함수가 있을수도있잖아….
    - 주로, *이 앞에 붙어있으면, 컴퓨터에서는 주로 **주소값**을 의미합니다

```bash
pwndbg>b *0x40129c
```

![image.png](image%20110.png)

# ni (next instruction)

breakpoint 에서 멈추고 나면 ni (next instruction) 이라는 명령어로 코드를 한줄 한줄 실행시킬 수 있습니다.

![image.png](image%20111.png)

![image.png](image%20112.png)

ni 를 계속 실행하다보면, 우리가 짠 photoDot 의 각 코드까지 도달합니다

### fopen 까지 도달한 모습

![image.png](image%20113.png)

![image.png](image%20114.png)

ni 를 계속 입력합니다…

### 메모리로 읽은 image 를 옮기면서 처리하는 모습

![image.png](image%20115.png)

ni 를 계속 입력합니다…

### dotty 에 도달

![image.png](image%20116.png)

# si (step into)

초록색으로 표시된 코드는 ni 를 누르면 실행되는 “아직 실행 안된” 코드입니다.

이때, 다음에 실행할 코드가 **call** 이면, 함수 안으로 들어가지는 않습니다. (이런걸 step over 라고 합니다. ni 는 step over 를 하는 명령어인거죠)

우리는 dotty 안이 궁금하니까, dotty 안으로 진입해야합니다.

초록색으로 표시된 코드가 call 일때, (함수 실행하는 코드일때) si 라는 명령어를 입력하면 함수 안으로 들어갑니다.

*dotty 함수에서 더 실행해버렸다면, b main 으로 main함수에 breakpoint 를 잡고, r 로 다시 실행해서 ni 를 해서 dotty 까지 가면 됩니다. 

```bash
gdb> si
```

짠 dotty 함수 안으로 들어와졌죠

![image.png](image%20117.png)

![image.png](image%20118.png)

# b dotty (breakpoint dotty)

![image.png](image%20119.png)

# disass

disass <함수이름> 명령어는 함수를 디스어셈블해줍니다.

```bash
pwndbg>disass main
pwndbg>disass dotty
```

![image.png](image%20120.png)

![image.png](image%20121.png)

# info functions

info functions 또는 i functions 명령어는 현재 메모리에 올라가 있는 함수와 그 주소를 모두 출력합니다

(i b 할때 그 i 입니다. i 뒤에 붙이면 정보를 보여주는거죠)

```bash
pwndbg>info functions
```

![image.png](image%20122.png)

![image.png](image%20123.png)

![image.png](image%20124.png)