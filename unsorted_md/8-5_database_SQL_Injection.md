# 8-5_database : SQL Injection

<aside>
💡 author : 전재호(agamtt) 2024-1-22

</aside>

# SQL injection 의 원리

SQL injection 은 쿼리문을 조작하여서 해킹을 하는 수법입니다.

아주 아주 다양한 injection 이 있기 때문에 모든 것을 여기에서 다루지는 않겠습니다.

일반적인 쿼리문은 아래와 같이 생겼습니다.

```sql
SELECT user FROM user_table WHERE id='입력한 아이디' AND password='입력한 비밀번호';
```

그러나 여기서, ‘입력한 아이디’ 와 ‘입력한 비밀번호’ 는 form 을 통해서 제출한 값입니다. 즉 사용자가 마음대로 넣을 수 있습니다.

## 주석

파이썬에서는 코드에 메모를 할 수 있는 기능이 있습니다. 그래서 코드에 설명을 달 수 있습니다. 편리하네요. # 을 입력하면 뒤에있는 것은 코드가 아니라 주석으로 해석되서 무효화 됩니다.

```php
print(student_age) # 학생의 나이를 출력
```

SQL 도 주석을 지원합니다. SQL 주석은 dash 두개 (--) 입니다. 이 기호 뒤의 내용은 무효화 됩니다.

```php
SELECT * FROM users; --users 테이블에 모든 레코드 출력
```

해커들은 이 주석기호 같은 특수한 역할을 하는 기호를 쿼리에 삽입해서 쿼리를 조작합니다.

주석기호를 삽입하는 기법은 SQL Comment Injection Attack 으로 불립니다.

고양이 홈페이지에서 해보기전에, check_database.php 에서 한번 실험해해보고 무슨일이 생기나 확인해봅시다.

```bash
<?php

    $db = new SQLite3('cat_homepage.db');

    $enteredUsername = "babo";
    $enteredPassword = "babo1234";

    // Query to check user credentials
    $query = "SELECT * FROM users WHERE username='{$enteredUsername}' AND password='{$enteredPassword}' ";
    $result = $db->query($query);

    // Check if the entered credentials are valid

    echo "your query : $query";
    echo "<br>";
    
    $row = $result->fetchArray();

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

여기서 쿼리문을 생성하는 부분은 아래와 같습니다.

```php
$enteredUsername = "babo";
$enteredPassword = "babo1234";
$query = "SELECT * FROM users WHERE username='{$enteredUsername}' AND password='{$enteredPassword}' ";
```

만약 틀린 패스워드를 넣으면, 로그인에 실패합니다.

```php

$enteredUsername = "babo";
$enteredPassword = "asdf";
$query = "SELECT * FROM users WHERE username='{$enteredUsername}' AND password='{$enteredPassword}' ";
```

![Untitled](Untitled%20558.png)

그러나, Comment(주석) 을 삽입하면 뒤에있는 쿼리를 무효로 만들 수 있습니다.

비밀번호 검증없이, 쿼리하여 레코드를 찾을 수 있습니다.

```php
$enteredUsername = "babo'--";
$enteredPassword = "asdf";
```

위의 입력값을 넣으면, 아래와 같은 쿼리문이 만들어집니다.

```sql
SELECT * FROM users WHERE username='babo'--' AND password='{$enteredPassword}' ";
```

-- 뒤부터는 주석이므로, 사실상 아래와 같습니다.

```sql
SELECT * FROM users WHERE username='babo';
```

비밀번호 검증을 우회해서, 쿼리가 작동합니다.

![Untitled](Untitled%20559.png)

# 고양이 홈페이지 SQL injection

엔드페이지 보안, 세션을 적용하고 보안에 신경 썼는데도 우리의 해커 babo 는 포기하지 않고 계속 grape 의 계정을 해킹하려고 시도합니다. 지긋지긋한 놈이네요.

아래의 공격코드를 삽입하여, SQL injection 을 수행합니다. 비밀번호는 아무거나 넣어도 상관없습니다. 어차피 주석이라서 실행 안되거든요.

```sql
grape'--
asdf
```

![Untitled](Untitled%20560.png)

이런, grape 유저의 개인페이지에 접속 성공하고 맙니다. 보안 사고네요

![Untitled](Untitled%20561.png)

# SQL Injection

SQL Injection 은 (아주 유명한) 해킹 기법입니다.

db 는 온갖 곳에 다 쓰이기 때문에, (회원정보 저장, 과속방지카메라 데이터 저장 등)

SQL Injection 은 지난 10년간 아주 많이 사용된 해킹 방법입니다.

게다가 실제 서비스에서는 여러개의 테이블과 복잡한 구조의 db가 사용되므로, 이것을 막는 것이 꽤 까다롭습니다.

![Untitled](Untitled%20562.png)

![Untitled](Untitled%20563.png)

![Untitled](Untitled%20564.png)

![Untitled](Untitled%20565.png)

계속