# mkdir / cat / rm

<aside>
💡 author : 전재호(agamtt) 2023-10-05

</aside>

<aside>
🔥 명령어를 연습하세요

모든 명령어는 여러번 사용하면서 익숙해져야합니다.

모든 실습 명령어를 여러번 사용하면서 연습하시기 바랍니다.

</aside>

경로를 이동하는 법을 배웠으니, 이제 폴더를 직접 만들어봅시다.

### mkdir

mkdir 은 make directory 의 약자입니다.

```bash
mkdir {directory_name}
```

/home/guest1 에 내맘대로 디렉토리를 만들어봅시다.

자기 이름으로 된 폴더를 만들어보세요.

```bash
mkdir eunmanChoi
```

이제 ls 를 해보면 만든 폴더가 표시됩니다.

![Untitled](Untitled%2032.png)

자기가 만든 폴더로 들어갈 수도 있습니다.

```bash
cd eunmanChoi
ls
```

ls 해보면 아무것도 없군요

### cat

cat 은 고양이가 아니고, catch 의 약자입니다.

cat 으로 파일을 읽거나, 생성할 수 있습니다.

```bash
cat {filename}
```

최상위 디렉토리에 위치한 helloHacker.txt 를 읽어봅시다.

전체 경로를 모두 입력하면 바로 읽을 수 있습니다.

```bash
cat /helloHacker.txt
```

![Untitled](Untitled%2033.png)

또는, cd 와 ls 로 이동한 후 경로 없이 읽어도 됩니다.

![Untitled](Untitled%2034.png)

cat 으로 파일을 생성해봅시다.

본인 이름으로 된 폴더로 돌아갑니다.

```bash
cd /home/guest1/eunmanChoi
```

```bash
cat > my_name_is_eunmanChoi.txt
```

그러면 텍스트를 입력할 수 있는 프롬프트가 열립니다.

아무 텍스트나 입력해봅시다.

![Untitled](Untitled%2035.png)

Ctrl + d 를 입력하면 저장됩니다.

다시 cat 으로 확인해보면,

```bash
cat {filename}
```

![Untitled](Untitled%2036.png)

텍스트가 저장된 것을 확인할 수 있습니다.

### rm

이제 내가 만든 것들을 삭제해봅시다.

rm 은 remove 의 약자로, 파일이나 폴더를 삭제할 수 있습니다.

폴더와 파일을 햇갈려서 폴더안의 파일이 전부 삭제되는 불상사를 막기 위해, rm 명령어로 파일을 삭제할 때는 옵션을 입력하지않고, 폴더를 삭제할때에는 옵션으로 “이것은 폴더다” 라고 알려줘야합니다.

**파일을 삭제할 때**

```bash
rm {file_name}
```

**폴더를 삭제할 때**

```bash
rm -r {file_name}
```

-r 은 recursive 의 약자로, 폴더 내부 전체를 의미합니다.

my_name_is_eunmanChoi.txt 파일을 삭제해봅시다.

파일이므로 옵션이 필요없습니다.

![Untitled](Untitled%2037.png)

이제 나가서 폴더를 삭제해봅시다.my

아까 말한 것 처럼, rm 을 옵션없이 사용하면 폴더를 삭제할 수 없습니다.

![Untitled](Untitled%2038.png)

-r 옵션을 입력해줍니다.

```bash
rm -r eunmanChoi
```

ls 해보면, 폴더가 삭제되었습니다.

![Untitled](Untitled%2039.png)

계속