# Graple Story : 고블린을 쓰러뜨리자

<aside>
⚠️ author : 전재호(agamtt) 2024-03-12

</aside>

![Untitled](Untitled%20283.png)

플레이어가 몬스터와 싸우는 대작 RPG, **Graple Story** 를 코딩해봅시다.

코드가 너무 길어서 숨이 막힐 지경이지만, 열심히 코딩해 봅시다.

아래는 완성본입니다.

```c
// graple_story_1.c 

#include <stdio.h>
#include <stdlib.h>

void printStatus(int first, int second, int third, int fourth){
    printf("\n");
    printf("현재 고블린 체력        : %d\n",first);
    printf("현재 고블린의 공격력    : %d\n",second);
    printf("--------------------------------------\n");
    printf("현재 플레이어 체력      : %d\n",third);
    printf("현재 플레이어의 공격력  : %d\n",fourth);
    
    printf("\n");
}

int main(){
    int playerHealth = 100;
    int playerAttack = 6;

    int enemyHealth = 20;
    int enemyAttack = 8;

    int playerAction = 0;

    printf("------------Graple Story--------------\n");
    printf("--------------------------------------\n");
    printf("\n");

    printf("고블린이 나타났습니다...\n");

    printStatus(enemyHealth,enemyAttack,playerHealth,playerAttack);

    while(1){
        printf("행동을 선택하세요 (0: 공격, 1: 방어): ");
        scanf("%d", &playerAction);
        printf("\n");

        if(playerAction == 0){
            printf("--------------------------------------\n");
            printf("공격을 선택했습니다.\n\n");
            printf("플레이어가 고블린을 공격!... 데미지 -%d\n",playerAttack);
            enemyHealth -= playerAttack;
            printf("고블린이 플레이어를 공격!... 데미지 -%d\n",enemyAttack);
            playerHealth -= enemyAttack;
            printStatus(enemyHealth,enemyAttack,playerHealth,playerAttack);
            printf("--------------------------------------\n");
        }

        if(playerAction == 1){
            printf("--------------------------------------\n");
            printf("방어를 선택했습니다.\n\n");
            printf("고블린이 플레이어를 공격!\n\n");
            printf("플레이어는 고블린의 공격을 방어했다...\n");
            printStatus(enemyHealth,enemyAttack,playerHealth,playerAttack);
            printf("--------------------------------------\n");
        }        

        if(enemyHealth < 0){
            printf("고블린을 쓰러뜨렸습니다. 신난다!!\n");
            break;
        }

        if(playerHealth < 0){
            printf("당신은 죽었습니다...\n");
            printf("게임 오버...\n");
            break;
        }

    }
    printf("--------------------------------------\n");
    printf("-----------게임을 종료합니다----------\n");
}

```

컴파일하고 실행해줍니다.

```bash
gcc -o graple_story_1 graple_story_1.c 
```

이제 소스코드는 삭제합니다. (rm 은 remove 의 약자입니다.)

```bash
rm graple_story_1.c
```

이 완성된 실행파일은 Grapple Story 공식 홈페이지에서 다운받아서 설치할 수 있습니다. 다운받았다치고, 게임을 플레이 해봅시다.

```bash
./graple_story_1
```

![Untitled](Untitled%20284.png)

공격과 방어를 적절히 사용하여, 고블린을 쓰러뜨리면 게임의 엔딩을 볼 수 있습니다.

![Untitled](Untitled%20285.png)

훌륭합니다.

Graple Story 1편은 사람들의 큰 호응을 얻어 무려 10억 장이 팔렸습니다.

인기에 힘입어, 제작사인 Jehoxon 은 2편을 제작하기로 했습니다.

계속 

<aside>
⚠️

Q) 아니 화면이 없는데 이게 뭔 게임인가요
A) 화면을 그리는 것을 그래픽 처리라고 부릅니다.

그래픽 처리하는 코드까지 짜면, 코드가 너무 길어져서 해킹 강의가 아니라 게임개발 강의가 되어버려서 생략했습니다.

다만, 실제 게임의 코드도, 그래픽을 보여주는 부분 빼고는 거의 동일합니다.

이 강의에서 배운 기술은 실제 게임에도 동일하게 적용됩니다

</aside>

![image.png](image%2014.png)