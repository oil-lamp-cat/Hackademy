# Quokka RAT : 쉘커맨드를 파이썬으로 실행하기 - subprocess

<aside>
⚠️ author : 전재호(agamtt) 2024-03-17

</aside>

이 글은 아래를 참고했습니다.

[subprocess — 서브 프로세스 관리](https://docs.python.org/ko/3/library/subprocess.html)

[[파이썬(Python)] #19. subprocess 모듈](https://answer-me.tistory.com/20)

해커의 컴퓨터에 [test.py](http://test.py) 라는 파일을 만들고, subprocess 모듈에 대해 알아봅시다.

subprocess 는 쉘커맨드를 python으로 실행합니다.

import 하여 사용할 수 있습니다.

subprocess.run() 함수는 명령어를 입력받고, 그 실행 결과를 반환합니다.

아래 코드를 실행하면, ls 명령어가 실행되고, 그 결과가 output.out 에 저장되어 출력됩니다.

```bash
import subprocess

# ls 명령어 실행
output = subprocess.run('ls', shell=True, stdout=subprocess.PIPE, text=True)

# 결과 출력
print(output.stdout)
```

![Untitled](Untitled%20583.png)

이제 터미널이 아니라 코드로 쉘커맨드를 사용할 수 있게 되었습니다.

계속