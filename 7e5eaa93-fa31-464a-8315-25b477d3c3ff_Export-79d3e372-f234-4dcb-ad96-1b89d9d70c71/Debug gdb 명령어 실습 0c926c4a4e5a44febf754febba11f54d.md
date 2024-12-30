# Debug : gdb 명령어 실습

<aside>
⚠️ author : 전재호(agamtt) 2024-03-15

</aside>

# 실행(run), 중단점(breakpoint)

프로그램을 실행하는 것을 디버거에서는 **실행(run)** 이라고 부릅니다.

디버거는 프로그램을 코드 한줄 한줄 멈춰가며 관찰하고 실행시킬 수 있습니다.

마치 실험실에 가둔 실험체처럼, 원하는 속도로 프로그램을 실행시켜보면서 작동원리를 분석하기 위한 기능입니다.

그러나 코드는 몇천 줄씩 되니까, 매 한줄 한줄마다 멈추는 것은 비효율적입니다.

따라서, 디버거는 멈출 코드를 지정하고, 해당 코드에서 말고는 안 멈춥니다.

멈추기로 설정한 코드를 **중단점(breakpoint)**이라고 부릅니다.

gdb 에서는 특정 함수나 코드를 gdb shell 명령어로 중단점(breakpoint) 로 설정합니다.

<aside>
💡 “breakpoint” 나 “중단점” 이라고 부르면 너무 기니까, bp 라고 짧게 부르기도 합니다.

</aside>

### r 명령어 (run)

실행(run)을 하는 방법은 아래와 같습니다. run 은 자주 쓰는 명령어라서 r 로 축약해서 써도, run 됩니다. 

```bash
gdb> run
# 또는
gdb > r
```

이미 run 된 상태에서 run 을 하면, 프로그램이 처음부터 재시작됩니다.

### b 명령어 (breakpoint)

b 는 breakpoint 의 약자로, 중단점을 설정합니다.

C언어로 만든 프로그램은 main 이라는 지점을 항상 갖고 있으니, 아래 명령어로 main 에 중단점을 설정합니다.

```bash
gdb> b main
```

만일, main 을 기준으로, main 이후에 124번째 줄의 코드에 중단점을 설정하고 싶다면,
C언어에서 주소 참조 연산자인 *를 사용하면 됩니다.

즉, 아래와 같이 쓰면 됩니다.

```bash
gdb> b *main+124
```

### i 명령어 (info)

i 는 설정된 값을 조회하는 명령어 입니다.

아래 명령어로 설정한 breakpoint 들을 조회할 수 있습니다.

```bash
gdb> i b
```

### del 명령어

i b 로 출력한 breakpoint 들을 삭제하는 명령어 입니다.

breakpoint 의 번호를 넣으면 해당 중단점이 삭제 됩니다.

```bash
gdb> i b # 설정된 breakpoint 들이 번호와 함꼐 출력됨
gdb> del 1 # 1번 breakpoint 가 삭제됨
```

### ni 명령어 (next instruction)

ni 명령어는 코드를 한줄 한줄 실행합니다.

```bash
gdb> ni
```

### c 명령어 (continue)

c 명령어는, 한 중단점에서 다음 중단점까지 멈추지 않고 계속 실행합니다.

```bash
gdb> c
```

# 실습

터미널의 크기를 조절할 수 있습니다.

gdb 는 출력되는 텍스트가 많으니, 최대한 위로 올려서 창의 크기를 키웁니다.

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

main+25 와 main+48 에 중단점을 설정해보겠습니다.

아래 명령어로 두개의 중단점을 설정하고 확인합니다.

```bash
gdb> b *main+25
gdb> b *main+48
gdb> i b
```

![Untitled](Untitled%20322.png)

이제 다시 r 을 하고, c 를 입력할때마다 각 중단점까지 실행됩니다.

```bash
gdb> r # 첫번째 중단점인 main+25 까지 실행됩니다.
gdb> c # 두번째 중단점인  main+48 까지 실행됩니다.
gdb> c # 더이상 중단점이 없으니, 프로그램이 계속 실행됩니다.
```

![Untitled](Untitled%20323.png)

![Untitled](Untitled%20324.png)

이제 quit 을 입력해서 나갑니다.

```bash
gdb> quit
```

이제 clear 까지 입력하면 gdb 가 출력했던 화면이 지워집니다.

```bash
clear
```

이 복잡한 화면들이 각각 무엇을 의미하는지 나중에 배울 것 입니다.

![Untitled](Untitled%20325.png)

계속