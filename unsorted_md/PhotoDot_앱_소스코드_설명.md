# PhotoDot 앱 소스코드 설명

<aside>
🧑🏻‍💻 author : 전재호(agamtt) 2024-03-12

</aside>

이 앱의 코드를 대충 설명해보겠습니다.

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

<aside>
⚠️

데이터를 저장하는 배열 file_buffer, filter_buffer 등을 “버퍼 메모리” 또는 “버퍼” 라고 부릅니다

</aside>

- 엔터가 입력되면 현재 폴더에서 “image” 라는 이름의 파일을 읽어서, img_content 버퍼에 저장합니다.
    - 파일이 없으면 “No File!” 에러를 출력합니다
- 파일을 닫습니다.
- dotty 함수를 실행합니다.
    - dotty 함수는 이미지를 도트 이미지로 바꿉니다!
- dotty 함수가 끝나면, “App Exit~” 을 출력하고 프로그램을 종료합니다

dotty 함수가 끝나고 나면 return 0 로 종료합니다.

<aside>
💡 **참고)**
이 코드가 이해가 가지 않는다면 C언어를 더 공부하고 와야합니다.

</aside>

아주 멀쩡해보이는 코드입니다.

이 시스템을 코딩한 소프트웨어 개발자는 코드를 완성하고 기분 좋은 마음으로 퇴근을 했을겁니다.

하지만 이 코드에는 **버퍼 오버플로우 취약점**이 있습니다.

이 프로그램을 해킹해봅시다…

계속…