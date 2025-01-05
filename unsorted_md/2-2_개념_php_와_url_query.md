# 2-2 개념 : php 와 url query

<aside>
💡 author : 전재호(agamtt) 2023-12-05

</aside>

index.html 은 일단 치워두고,

php 의 기초를 익혀보자.

# PHP

<aside>
💡 php 는 웹을 만드는데 쓰이는 프로그래밍 언어이다.

</aside>

php 코드파일은 .php 이다.

php 로 코드를 짠 후, php 명령어를 이용하여 서버를 작동시키면, **브라우저로 해당 php 파일을 요청했을때 해당 php 파일이 실행된다**.

## PHP 파일 실행해보기

index.html 이 있는 디렉토리에 test.php 를 만든다.

php 는 html 안에 삽입되어서 사용되고, php 태그라는 것으로 둘러싸면 안에 있는 모든 것은 php 코드가 된다.

echo 는 php 로 웹페이지에 문자열을 출력한다 (python 의 print 와 같다.)

php 문은 반드시 세미콜론(;)으로 끝나야한다.

```php
<?php
echo "hello php!";
?>
```

php 서버를 실행한다.  (index.html, test.php 가 있는 디렉토리에서 명령어를 실행해야함)

```php
php -S 0.0.0.0:8000
```

웹브라우저로 접속한다. 이때, php 파일을 달라고 한다. 그러면 **php 코드가 실행된다.**

```php
localhost:8000/test.php
```

문자열이 잘 출력되는 것을 확인할 수 있다.

![Untitled](Untitled%20403.png)

# php 변수

python 과 마찬가지로 php 에서는 변수를 설정할 수 있다. 변수에는 숫자, 문자열 등의 값이 저장된다.

python 과 다른 점은, php 에서 모든 변수 앞에는 달러($) 표시가 붙는다. 반대로, 달러표시가 있는 모든 것은 변수이다.

```php
<?php
$name = "John";
$iq = 13;
echo "hello $name your IQ is $iq!";
?>
```

![Untitled](Untitled%20404.png)

# URL query

<aside>
💡 URL query 는 웹의 기본중의 기본이다. 우리는 알게 모르게 매일 URL query 를 사용하고 있다.

</aside>

query 의 que 는 질문(question) 의 que 이다.

URL 뒤에 ? 를 붙이면 php 에 변수값을 전달할 수 있다.

query 라는 이름이 붙은 이유는 처음 만들어질때 주로 도서 검색 시스템 같은거에서 내가 찾는 책을 내놔 라는 기능으로 쓰였기 때문이다. 

이 url 쿼리를 통해, 브라우저와 서버가 값을 주고 받을 수 있다. 모든 웹서버는 URL query 값을 읽는 기능을 가지고 있다.

php 로 url 쿼리를 읽어봅시다.

브라우저에서 url query 를 보내려면 url 뒤에 ? 를 붙이고, 변수와 값을 = 으로 연결한다. 각 변수는 & 로 구분한다.

```php
localhost:8000/test.php?name=gaeun&iq=50
```

php 에서는 $_GET[] 의 대괄호 안에 query 변수명을 넣으면 된다. 위의 쿼리를 받으려면 이렇게 한다.

```php
<?php
echo $_GET['name'];
echo  $_GET['iq'];
?>
```

![Untitled](Untitled%20405.png)

이렇게 받는 URL query 는 변수에 저장될 수 있다. 이를 통해 문장을 만들어보자.

브라우저:

```php
localhost:8000/test.php?name=gaeun&iq=50
```

test.php:

```php
<?php

$your_name = $_GET['name'];
$your_iq = $_GET['iq'];

echo "your name is $your_name, and your IQ : $your_iq"

?>
```

![Untitled](Untitled%20406.png)

<aside>
💡 즉, 우리는 url query 를 이용해서, 웹브라우저로 서버에 값을 전송할 수 있고, 서버에서 그 값을 변수명으로 불러올 수 있다는 것을 알았습니다.

</aside>

계속