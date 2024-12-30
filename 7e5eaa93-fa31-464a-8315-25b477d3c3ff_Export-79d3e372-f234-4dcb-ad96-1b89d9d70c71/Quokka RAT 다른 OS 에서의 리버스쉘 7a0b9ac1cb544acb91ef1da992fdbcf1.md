# Quokka RAT : 다른 OS 에서의 리버스쉘

<aside>
⚠️ author : 전재호(agamtt) 2024-03-17

</aside>

# Quokka RAT

리눅스에서 작동하는 RAT 을 제작해봤습니다.

거의 모든 컴퓨터에 대한 RAT 을 제작할 수 있습니다.

그러나, 운영체제에 따라 코드를 약간 변경해야합니다.

우리의 RAT 은 subprocess() 함수를 사용하니, 이 부분만 약간 수정하면 됩니다.

아래는 단순히 소개만 하니, 실습해보지 않아도 됩니다.

# Windows 에서 subprocess

cmd 를 실행하는 subprocess

```bash
import subprocess

# cmd를 사용하여 ls 명령어 실행
result = subprocess.run(['cmd.exe', '/c', 'dir'], stdout=subprocess.PIPE, text=True)

# 결과 출력
print(result.stdout)

```

powershell 을 실행하는 subprocess

```bash
import subprocess

# PowerShell을 사용하여 ls 명령어 실행
result = subprocess.run(['powershell.exe', '-Command', 'ls'], stdout=subprocess.PIPE, text=True)

# 결과 출력
print(result.stdout)

```

# MacOS 에서 subprocess

bash 쉘을 실행하는 subprocess

```bash
import subprocess

# Bash를 사용하여 ls 명령어 실행
result = subprocess.run(['/bin/bash', '-c', 'ls'], stdout=subprocess.PIPE, text=True)

# 결과 출력
print(result.stdout)

```

아래와 같은 사이트에서 목록을 확인해볼 수 있습니다.

[GitHub - swisskyrepo/PayloadsAllTheThings: A list of useful payloads and bypass for Web Application Security and Pentest/CTF](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master)

[Reverse Shell Cheat Sheet - Internal All The Things](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/)

계속