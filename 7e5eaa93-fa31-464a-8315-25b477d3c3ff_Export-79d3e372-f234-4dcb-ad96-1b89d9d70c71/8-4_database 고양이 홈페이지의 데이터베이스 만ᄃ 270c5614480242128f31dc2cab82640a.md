# 8-4_database : 고양이 홈페이지의 데이터베이스 만들기

<aside>
💡 author : 전재호(agamtt) 2024-1-22

</aside>

# php-sqlite3 설치

<aside>
💡 php 안에서 sqlite3 를 연결하기 위해 필요합니다

</aside>

sqlite3 를 사용하기 위해 sqlite3 런타임을 apt 로부터 설치합니다.

아래 명령어를 이용해 설치합니다

```bash
sudo apt install -y sqlite3 php-sqlite3
```

# db 파일 만들기

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

    $query = "SELECT * FROM users WHERE username='{$enteredUsername}' AND password='{$enteredPassword}' ";
    $result = $db->query($query);

    echo "your query : $query";
    echo "<br>";

    if ($result->fetchArray()) {
        echo "this is on database : $enteredUsername/$enteredPassword";
        echo $result->fetchArray();
    }else{
        echo "CAUTION not in database : $enteredUsername/$enteredPassword";
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

# 데이터베이스 연결

index.php 맨 위에 아래를 추가합니다.

```php
<?php
session_save_path('./');
session_start();

// SQLite 데이터베이스 연결
$db = new SQLite3('cat_homepage.db');

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the entered username and password
    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];

    // Query to check user credentials
    $query = "SELECT * FROM users WHERE username='{$enteredUsername}' AND password='{$enteredPassword}' ";
    $result = $db->query($query);
    $row = $result->fetchArray();

    // Check if the entered credentials are valid
    if ($row) {
        // Redirect to the login success page
        $login_user = $row["username"];
        $_SESSION["user"] = $login_user;
        header("Location: page-{$login_user}.php");
        exit();
    } else {
        // Invalid credentials, you might want to display an error message
        $errorMessage = "Invalid username or password";
    }
}
?>
```

# db 파일 열기

try catch 문을 이용해서 알 수 없는 이유로 데이터베이스 연동이 실패하는 경우 에러를 출력하도록 합니다.

```sql
<?php

// SQLite 데이터베이스 연결
try {
    $db = new SQLite3('cat_homepage.db');
} catch (Exception $e) {
    die("Database connection failed: " . $e->getMessage());
}
```

# db 를 통해 로그인 정보 쿼리 및 인증

form 으로 부터 온 post request 에서 username 과 password 값을 $enterdUsername 과 $enterdPassword 에 각각 저장합니다.

```bash
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the entered username and password
    $enteredUsername = $_POST["username"];
    $enteredPassword = $_POST["password"];
```

- $query 는 form 으로부터 온 post http request 의 $enteredUsername 과 $enteredPassword 로 쿼리문을 생성합니다.
- result 는 db 에 쿼리한 결과를 저장합니다.
- row 는 result 를 php 배열로 바꾼 것 입니다.

```bash

    $query = "SELECT * FROM users WHERE username='{$enteredUsername}' AND password='{$enteredPassword}' ";
    $result = $db->query($query);
    $row = $result->fetchArray();
```

- $row 에서 “username” 으로 검색하여 grape 를 얻습니다. 이것을 $login_user 에 저장합니다.
- 이를 세션파일에 user 로 저장합니다.
- header() 를 이용하여 page-{$login_user}.php 로 리다이렉트 시킵니다.
    - grape 가 user 이면 page-grape.php 로 이동되겠네요.

```bash

    if ($row) {
				$login_user = $row["username"];
        $_SESSION["user"] = $login_user;
        header("Location: page-{$login_user}.php");
        exit();
    } else {
        $errorMessage = "Invalid username or password";
    }
```

# 테스트

실행해보면,

![Untitled](Untitled%20556.png)

![Untitled](Untitled%20557.png)

잘 작동합니다!

이제 db 를 사용하는 사이트이니, 몇천명, 몇만명이 가입되어있더라도 새로 코딩할 필요가 없습니다.

게다가 서버의 코드를 바꿔도, db 파일이 똑같으면 유저 정보를 유지할 수 있겠네요.

그러나 이 설계에는 치명적인 보안 결함이 있습니다.

SQL Injection 을 이용해서 해킹해봅시다.

계속