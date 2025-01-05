# scanf 는 아주 유명한 버퍼오버플로우임

**scanf 에서도 똑같은 일이 벌어집니다.**

C언어를 학교나 학원에서 배워본 사람이라면 scanf 를 사용하면 경고가 발생하는 경험을 해봤을겁니다.

이런 코드를 짜고 컴파일 해준다음,

```c
// gcc -o hello hello.c -fno-stack-protector -no-pie

#include <stdio.h>

void hidden(){
    printf("THIS SHOULD NOT BE ACCESSED!!!\n");
	fflush(stdout);
}

int main(){
    char buffer[10];

    printf("hello, input : ");
    scanf("%s", buffer);
	printf("your input : %s\n",buffer);

    return 0;
}
```

실행해주면,

```bash
./hello
```

scanf 가 키보드 입력을 받아서 버퍼에 저장하는 작은 프로그램을 만들 수 있습니다. 보통 C언어 첫시간에 하는 실습인데요

![image.png](image%20158.png)

scanf 는 사실 **파일**도 입력으로 받을 수 있습니다.

cute_file.txt 라는 파일을 만들고, 이렇게 쓴다음

```
Hello~ I am little file
```

```
./hello < cute_file.txt
```

이러면 키보드입력 대신 해당 파일의 내용이 입력됩니다 

![image.png](image%20159.png)

# scanf 스택 버퍼오버플로우 공격

실행시킬 코드의 기계어가 적힌 주소를 찾아내서,

```
objdump -d hello
```

![image.png](image%20160.png)

exploit 이라는 파일을 만들고 바이너리에 원하는 주소로 덮어씌우고,

![image.png](image%20161.png)

해당 데이터를 입력으로 집어넣으면,

![image.png](image%20162.png)

**스택 버퍼 오버플로우**가 일어나서 **코드 흐름이 조작**됩니다.