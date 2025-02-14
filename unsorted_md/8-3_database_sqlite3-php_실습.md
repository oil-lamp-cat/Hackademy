# 8-3_database : sqlite3-php 실습

<aside>
💡 author : 전재호(agamtt) 2023-12-20

</aside>

이제 만든 db 파일과 php 를 연동해봅시다.

index.php 에 바로 연결하기 전에, 작은 php 코드들을 만들어서 어떻게 작동하는지 먼저 확인해봅시다.

우선 cat_homepage.db 라는 디비를 만듭니다.

아래 리눅스 명령어를 입력합니다.

```bash
sqlite3 cat_homepage.db
```

그리고 sqlite3 인터프리터에 아래 쿼리문을 입력해서, 테이블을 생성합니다.

```bash
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
```

아래 쿼리문으로 users 테이블이 잘 생성되었는지 체크해봅니다.

```bash
.tables
```

생성된 테이블에 유저의 레코드를 삽입 합니다. 세개만 넣어봅시다.

```bash
INSERT INTO users (username, password) VALUES ('grape', 'secret1234');
INSERT INTO users (username, password) VALUES ('alice', 'alice!@');
INSERT INTO users (username, password) VALUES ('babo', 'babo1234');
```

아래 쿼리문으로 users 테이블에 유저의 레코드가 잘 삽입되었는지 체크해봅니다.

```bash
SELECT * FROM users;
```

이제 sqlite3 인터프리터에서 나갑니다. 아래 명령어를 입력합니다.

```bash
.quit
```

cat_homepage.db를 확인하면 users 테이블에 유저 정보 record 가 삽입되어있음을 확인할 수 있습니다.

![Untitled](Untitled%20551.png)

# php 와 sqlite3 연동

check_database.php 라는 파일을 만들고 아래와 같이 입력합니다.

```bash
<?php

    $db = new SQLite3('cat_homepage.db');

    $enteredUsername = "grape";
    $enteredPassword = "secret1234";

    $query = "SELECT * FROM users WHERE username='" . $enteredUsername . "' AND password='" . $enteredPassword . "'";
   
		$result = $db->query($query);
	  $row = $result->fetchArray();
   

    echo "your query : $query";
    echo "<br>";
    
   

    echo "row : $row <br>";
    echo "<br>";
    
    echo "row['username'] : {$row['username']} <br>";
    echo "row['password'] : {$row['password']} <br>";

    echo "<br>";

    if ($row) {
        echo "this is on database : $enteredUsername/$enteredPassword";
        echo $result->fetchArray();
    }else{
        echo "not in database : $enteredUsername/$enteredPassword";
    }

?>
```

아래 코드는 cat_homepage.db 를 sqlite3 형식으로 열고, $db 라는 변수에 저장합니다.

```bash
$db = new SQLite3('cat_homepage.db');
```

SQLite3() 함수는 php-sqlite3 가 리눅스에 설치되어있어야 사용할 수 있습니다.

```bash
sudo apt install -y php-sqlite3
```

아래 코드는 쿼리문을 생성해서 db 에 입력합니다.

```bash
    $enteredUsername = "grape";
    $enteredPassword = "secret1234";

    $query = "SELECT * FROM users WHERE username='{$enteredUsername}' AND password='{$enteredPassword}' ";
```

php 에서 대괄호를 사용하면 문자열에 변수의 문자열을 대입할 수 있습니다.

아래 두 코드는 동일하게 동작합니다.

```bash
$enteredUsername = "grape";
$enteredPassword = "secret1234";

$query = "SELECT * FROM users WHERE username='{$enteredUsername}' AND password='{$enteredPassword}' ";
```

```bash
$query = "SELECT * FROM users WHERE username='grape' AND password='secret1234' ";
```

쿼리문이 실행되면 웹브라우저에 db 검색결과를 출력합니다.

- $result = $db->query($query); 는 쿼리 결과를 result 변수에 저장합니다
- $row = $result->fetchArray(); 는 result 를 php 가 읽을 수 있는 배열로 변환하여 row 변수에 저장합니다

if($row) 는 해당 레코드가 존재할 때에만 실행되므로 this is on database 를 출력하도록 했습니다.

```bash
$result = $db->query($query);
$row = $result->fetchArray();
...중략...
if ($row) {
        echo "this is on database : $enteredUsername/$enteredPassword";
        echo $result->fetchArray();
    }else{
        echo "not in database : $enteredUsername/$enteredPassword";
    }

?>
```

이제, 쿼리문이 실행되어 존재하는 레코드가 검색되면, 이것이 $row 배열에 저장됩니다.

$row 배열에 속성을 넣어서 검색하면 값이 출력됩니다.

아래는 쿼리결과인 row 에 username 속성으로 검색하는 php 코드입니다.

```bash
$row['username']
```

실행해봅시다.

# 테스트

check_database.php 엔드포인트로 접속하면, 아래와 같이 db 에 있는 정보를 php 가 쿼리하여 출력합니다.

```bash
SELECT * FROM users WHERE username='grape' AND password='secret1234'
```

이 쿼리문은 아이디가 grape 고 password 가 secret1234 인 레코드를 검색하라는 쿼리문입니다.

![Untitled](Untitled%20552.png)

디비에서 검색에 성공하여 this is on database 가 출력됩니다.

쿼리에 입력되는 user 와 password 를 바꿔봅시다.

우리가 테이블에 삽입했던 다른 레코드인 'alice', 'alice!@' 를 입력하면,

![Untitled](Untitled%20553.png)

디비에서 검색에 성공하여 this is on database 가 출력됩니다.

존재하지 않는 유저를 입력하면,

![Untitled](Untitled%20554.png)

![Untitled](Untitled%20555.png)

존재하지 않는 유저라고 나옵니다.

이제 이것을 고양이 홈페이지에 적용시켜봅시다.

계속