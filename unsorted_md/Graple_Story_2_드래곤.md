# Graple Story 2 : 드래곤

<aside>
⚠️ author : 전재호(agamtt) 2024-03-12

</aside>

플레이어가 몬스터와 싸우는 대작 RPG, **Graple Story 2** 를 코딩해봅시다.

![Untitled](Untitled%20286.png)

아래는 완성본입니다.

```c
// grapple_story_2.c

#include <stdio.h>
#include <stdlib.h>

void printStatus(int first, int second, int third, int fourth){
    printf("\n");
    printf("현재 드래곤 체력        : %d\n",first);
    printf("현재 드래곤의 공격력    : %d\n",second);
    printf("--------------------------------------\n");
    printf("현재 플레이어 체력      : %d\n",third);
    printf("현재 플레이어의 공격력  : %d\n",fourth);
    
    printf("\n");
}

int main(){
    int playerHealth = 100;
    int playerAttack = 6;

    int enemyHealth = 200;
    int enemyAttack = 30;

    int playerAction = 0;

    printf("------------Graple Story--------------\n");
    printf("--------------------------------------\n");
    printf("\n");

    printf("드래곤이 나타났습니다...\n");

    printStatus(enemyHealth,enemyAttack,playerHealth,playerAttack);

    while(1){
        printf("행동을 선택하세요 (0: 공격, 1: 방어): ");
        scanf("%d", &playerAction);
        printf("\n");

        if(playerAction == 0){
            printf("--------------------------------------\n");
            printf("공격을 선택했습니다.\n\n");
            printf("플레이어가 드래곤을 공격!... 데미지 -%d\n",playerAttack);
            enemyHealth -= playerAttack;
            printf("드래곤이 플레이어를 공격!... 데미지 -%d\n",enemyAttack);
            playerHealth -= enemyAttack;
            printStatus(enemyHealth,enemyAttack,playerHealth,playerAttack);
            printf("--------------------------------------\n");
        }

        if(playerAction == 1){
            printf("--------------------------------------\n");
            printf("방어를 선택했습니다.\n\n");
            printf("드래곤이 플레이어를 공격!\n\n");
            printf("플레이어는 드래곤의 공격을 방어했다...\n");
            printStatus(enemyHealth,enemyAttack,playerHealth,playerAttack);
            printf("--------------------------------------\n");
        }        

        if(enemyHealth < 0){
            printf("드래곤을 쓰러뜨렸습니다. 신난다!!\n");
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
gcc -o graple_story_2 graple_story_2.c 
```

이제 소스코드는 삭제합니다. (rm 은 remove 의 약자입니다.)

```bash
rm graple_story_2.c
```

이 완성된 실행파일은 Grapple Story 공식 홈페이지에서 다운받아서 설치할 수 있습니다. 다운받았다치고, 게임을 플레이 해봅시다.

```bash
./graple_story_2
```

![Untitled](Untitled%20287.png)

드래곤을 쓰러뜨릴때까지 계속 플레이 하세요.

```bash
./grapple_story_2
```

훌륭합니다.

![Untitled](Untitled%20288.png)

# 망겜

<aside>
💡

이 게임은 잘못 개발됐습니다.

</aside>

Grapple Story 2편은 망해버렸습니다.

망한 게임을 **망겜(Bullshit Game)** 이라고 부릅니다.

무슨 짓을 해도 "드래곤” 은 절대 이길 수 없습니다…. 

젠장…

이 망겜을 클리어할 좋은 방법이 없을까요?

한가지 아이디어는 핵을 만드는 것입니다. 게임을 해킹해서 치트(Cheat, 꼼수) 를 써서 게임을 깨봅시다

계속