# Binary Ninja 로 코드 패치하는 법

# Binary Ninja

graple_story_2 를 다시 정적분석해봅시다.

Binary Ninja 로 바이너리를 확인해보면, 맨 앞에 메모리의 특정 위치로 어떤 값들을 옮기는 (mov) 것을 볼 수 있습니다.

![image.png](image%2046.png)

대괄호로 둘러쌓인 하늘색 텍스트는, 디스어셈블러인 Binary Ninja 가 생성한 것 입니다.

이것을 뭐라고 부를지 Symbol 이 없으니 내가 우선 이렇게 부르겠다라고 랜덤하게 생성한 것 입니다.

이것을 **자동 변수명**(auto-generated variable names) 이라고 부릅니다.

![image.png](image%2047.png)

# 리네이밍 (Renaming)

- 소스코드에서 개발자가 만든 변수명은 컴파일 과정에서 사라집니다.
    - 이것을 심볼 제거라고 합니다.

![image.png](image%2048.png)

따라서 디스어셈블러는 바이너리만 보고는 변수명을 알 수 없습니다.

변수의 이름은 모르지만, 우리는 실행해보고, 그 용도를 추측해볼 수 있습니다. 개발자가 그걸 왜 선언했는지를 거꾸로 추측하는거죠

실행해본 우리는 이제 압니다. 

이 변수들은 플레이어와 드래곤의 체력의 값을 설정하는 코드라는걸요

 이제 분석하기 쉽도록 우리가 이 자동생성된 이름들을 수정할 수 있습니다. 

하늘색 부분을 더블클릭하면 수정할 수 있게 됩니다.

![image.png](image%2049.png)

![image.png](image%2050.png)

나머지도 분석한 내용을 바탕으로 추측해서 적어둡니다.

![image.png](image%2051.png)

그러면 나중에 player_heath 값이 또 쓰였을때 대괄호 안에 있는 변수명을 보고 쉽게 알 수 있겠습니다.

# 디스어셈블러로 코드 수정

Binary Ninja 등의 리버싱툴로도 코드패치를 할 수 있습니다.

클릭하고 단축키 e 를 누르거나, 우클릭을 하고 Patch - Edit Current Line 을 하면 됩니다.

![image.png](image%2052.png)

![image.png](image%2053.png)

![image.png](image%2054.png)

# 코드 패치 저장

이제 File - Save As 를 눌러서 바꾼 바이너리를 저장합니다.

이 바이너리에는 플레이어의 체력이 0x99, 십진수로 153 으로 바뀌었습니다.

![image.png](image%2055.png)

![image.png](image%2056.png)

이름은 뭐 graple_story_2_cheat 정도로 해줍니다

![image.png](image%2057.png)

<aside>
💡

다른 리버싱툴에서 똑같은 기능을 어떻게 사용하는지는, Google 이나 공식문서에 검색하면 나오겠죠?

</aside>

이제 치트가 적용된 게임을 해봅시다.

Linux 환경에서만실행할 수 있으니, 

패치된 파일을 드래그해서 docker container 로 옮겨줍니다.

visual studio code 에서는 드래그로 파일을 옮길 수 있습니다.

![image.png](image%2058.png)

이제 실행하려고 하면, 실행되지 않습니다.

이것은 이 파일이 외부에서 다운받아진 파일이므로, 실행권한이 없기 때문입니다.

![image.png](image%2059.png)

chmod 로 실행권한을 추가해줍니다

```bash
chmod +x 파일명
```

![image.png](image%2060.png)

이제 실행해보면 잘 실행되며, 치트가 적용된 것을 볼 수 있습니다.

```bash
./graple_story_2_cheat
```

![image.png](image%2061.png)