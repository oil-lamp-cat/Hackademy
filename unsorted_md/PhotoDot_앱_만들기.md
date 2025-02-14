# PhotoDot 앱 만들기

<aside>
🧑🏻‍💻 author : 전재호(agamtt) 2024-03-12

</aside>

![앱 아이콘은 chatGPT 로 만들었습니다…](Untitled%201.png)

앱 아이콘은 chatGPT 로 만들었습니다…

아래와 같이 코딩하고, 컴파일합니다.

파일이름은 photoDot 으로 합시다. photoDot.c 파일을 만들고,

(photoDot 이라는 디렉토리를 만들고 안에다가 모아놓으면 보기 좋겠죠? 보통 /home/ 아래에 만듭니다.

/home/photoDot/photoDot.c

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

 

아래 명령어를 입력해서 컴파일합니다.

```bash
gcc -o photoDot photoDot.c -fno-stack-protector -no-pie -zexecstack
```

<aside>
💡 **엥 -fno-stack-protector -no-pie -zexecstack 이건 뭔가요**

해커들이 지난 30년 간 C언어로 된 프로그램을 메모리 관련된 해킹으로 잔뜩 괴롭혔으므로, gcc 컴파일러는 기초적인 공격에 대한 방어기능을 제공합니다.

pwnable 대부분 이런 방어기능을 어떻게 우회할 것인가에 대해 다룹니다.

우선 처음엔 원리를 알아야하니 방어기능을 다 끄고 시작해봅시다.
방어 기능을 처음부터 뚫을 수 있으면 그게 방어기능이겠습니까?

이 명령어들은 방어기능을 끄는 명령어 입니다.

**-fno-stack-protector : 스택 프로텍터 해제 (스택 카나리아)
-no-pie : 메모리 주소공간 난독화 해제
-zexecstack : 런타임 메모리 실행 보호 해제**

당장은 뭔지 몰라도 됩니다!

</aside>

이 프로그램은 image 라는 이름의 파일을 읽어서 연 후,

점자로 된 그림으로 변환합니다. 즉,  “필터” 를 씌웁니다.

image  라는 파일을 만들고, 아래와 같이 입력합니다. 

*당나귀임

```

   //
 _oo\
(__/ \  _  _
   \  \/ \/ \
   (         )\
    \_______/  \
     [[] [[]
     [[] [[]    

```

![image.png](image%20101.png)

image 파일과 photoDot 실행파일을 **같은 디렉토리에 놓고** 실행하면,

![image.png](image%20102.png)

이렇게 이미지를 도트 이미지로 변환합니다.

이미지 편집 프로그램을 실제로 만드는 건 귀찮은 일이여서 간단하게 도트로 걍 했습니다.

[ASCII Art Archive](https://www.asciiart.eu/)

여기에서 다양한 그림을 가져와서 도트로 바꿔보세요

```
   ((...)) 
   ( O O ) 
    \   /  
    (`_`)   
```

```
  ______
 /|_||_\`.__
(   _    _ _\
=`-(_)--(_)-' 
```

실제 이미지 관련된 소프트웨어는 이 프로그램과 동일한 원리로 작동합니다.

- 사진이나 이미지를 불러온 후, 메모리에 저장 (이 메모리를 버퍼라고 부릅니다.)
- 버퍼에 있는 메모리를 이리 저리 바꾼다. (필터를 씌운다던지, 도트로 바꾼다던지)
- 버퍼에 있는 메모리(변환된 이미지)를 출력하거나 저장

우리는 출력으로 터미널을 사용합니다. 텍스트로 출력된다는거죠

터미널에 텍스트로 출력되는 것을 standard out 이라고 부릅니다.

C언어에서는 stdio.h 안에 있는 printf 함수로 할 수 있죠

실제 사진앱들은 Android 나 IOS 의 앱 화면을 그리는 GUI API 를 call 해서 화면에 사진을 표시합니다. 필터를 적용하는 부분은 똑같습니다.

그런 앱으로는 SNOW 앱이나 포토샵 등이 있겠네요.

![Untitled](Untitled%20377.png)

![Untitled](Untitled%20378.png)

당나귀 그림말고 다른 텍스트 아트를 써도 됩니다.

[ASCII Art Archive](https://www.asciiart.eu/)

여기 들어가서 확인해보면 많이 있습니다.

<aside>
💡 **엥 아니 이게 어떻게 사진 필터 앱이죠; 아스키 아트인데요**

코드가 길어져서 단순화하려고 아스키 아트로 했지만,

실제 사진이나 동영상에 필터를 적용하는 소프트웨어 요소와 완전히 원리가 같습니다.

사진 파일은 바이너리이고, 실제 이미지 관련 프로그램은 안에 있는 바이너리를 소프트웨어가 읽은 후 수정하는 방식으로 작동합니다.

</aside>

![image.png](image%20103.png)

![image.png](image%20104.png)

계속…