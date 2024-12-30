# 파일 수정하기 : vim / nano

<aside>
💡 author : 이명현(camellia) 2023-09-26
contributor : 노주형(jhnoh1) 2023-09-26 / 전재호(agamtt) 2023-10-05

</aside>

cat 은 간단한 파일을 쓰기에는 편리하지만, 긴 글을 쓰기에는 불편합니다.

리눅스에는 수많은 문서 작성 프로그램이 있지만, vim 과 nano 가 가장 흔히 쓰입니다.

# vim

Vim 은 리눅스에서 사용하는 메모장 프로그램입니다.

![Untitled](Untitled%2045.png)

파일명을 지정하여 텍스트파일을 생성할 수 있습니다.

```bash
vim {file_name}
```

![Untitled](Untitled%2046.png)

![Untitled](Untitled%2047.png)

명령어를 사용 하게 되면 이렇게 빈 메모장 같은 화면이 표시 됩니다. 

### 모드

리눅스에서는 마우스를 사용하지 못하니, “모드”라는 것으로 메뉴를 이동하고 선택합니다.

![Untitled](Untitled%2048.png)

현재 어떤 모드에 있는지 좌측하단에 표시됩니다.

아무것도 표시되지 않으면 기본모드 상태인 것입니다.

![Untitled](Untitled%2049.png)

i : 입력모드로 들어갑니다. 

![Untitled](Untitled%2050.png)

우측하단에 — INSERT — 가 표시됩니다.

![Untitled](Untitled%2051.png)

이제 문서를 편집할 수 있습니다.

아무 문서나 작성해봅시다.

![Untitled](Untitled%2052.png)

esc : 어느 모드에 있던 기본 모드로 돌아갑니다.

esc를 누르면 —INSERT— 가 사라지는 것을 확인할 수 있습니다.

![Untitled](Untitled%2053.png)

### 파일 저장

파일 저장이나 vim 나가기를 하기 위해서는 vim 명령어를 입력해야합니다.

: (콜론) 을 입력하면 명령어 모드가 됩니다.

:명령어 를 입력하고 enter를 치면 명령어가 실행됩니다.

![Untitled](Untitled%2054.png)

vim 에서 사용할 수 있는 명령어는 구글에 검색하면 전체를 볼 수 있습니다.

자주 쓰는 명령어만 외워서 쓰면 됩니다.

```bash
:w 는 파일을 저장합니다.(write의 약자)
:wq 는 파일을 저장하고, vim을 종료합니다. (write and quit)

:q! 는 파일을 저장하지 않고 강제로 종료합니다.
```

![Untitled](Untitled%2055.png)

엔터를 치면 종료됩니다.

파일을 저장하고 종료한 뒤, cat으로 입력한 내용을 확인할 수 있습니다.

![Untitled](Untitled%2056.png)

서버가 지저분해지니 rm 으로 사용한 파일은 삭제합시다.

```bash
rm {file_name}
```

# nano

nano 역시 vim 과 같은 텍스트 편집기이며, vim 에 비해서 친절한 편입니다.(화면 아래쪽에 단축기들이 다  써있음)

vim 과 nano 중 맘에 드는 걸 쓰시면 됩니다.

계속