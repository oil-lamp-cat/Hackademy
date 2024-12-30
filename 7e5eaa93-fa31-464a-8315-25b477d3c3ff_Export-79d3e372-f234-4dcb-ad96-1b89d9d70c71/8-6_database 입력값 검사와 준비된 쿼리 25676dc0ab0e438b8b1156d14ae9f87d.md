# 8-6_database : 입력값 검사와 준비된 쿼리

<aside>
💡 author : 전재호(agamtt) 2024-1-26

</aside>

# 입력값 검사 (Input Validation 또는 Input Sanitization)

sql injection 을 방어하는 간단한 방법중 하나는, 주석기호를 찾아서 없애버리는 겁니다.

str_replace() 함수는 특정 문자열을 찾아 다른 문자열로 바꿀 수 있습니다.

“” (빈 문자열)로 바꾸면, 해당 문자열이 제거 됩니다.

```php
$userInput = "some value -- with comment";

$cleanInput = str_replace("--", "", $userInput);

echo $cleanInput;
```

request 로 부터 들어온 form post 입력은 “외부에서 들어온 값” 입니다.

일반인도 입력할 수 있지만, 해커도 입력할 수 있습니다.

이렇게 외부에서 들어온 값을 신뢰해서는 안됩니다.

이렇게 어떤 조치를 통해, 외부에서 들어온 값을 안전하게 바꾸는 것이 마치 소독하는 것과 같다고 해서 소독(Sanitization) 이라고 부릅니다. 컴퓨터 보안에서는 SQL injection 말고도, 다양한 입력을 Sanitize 합니다.

# Prepared Statements

SQL injection 은 악명 높은 해킹기법이여서, 다양한 방어가 고안되었습니다.

그중 하나는 준비된 쿼리문(Prepared Statements) 을 사용하는 것 입니다.

Prepared Statements 는 두 단계에 걸쳐서 쿼리문을 생성합니다.

check_database_secure.php 를 만들어서 테스트해봅시다.

bindValue 는 특정 문자열을 해당 문자열로 치환합니다. 이때, 규칙을 지정할 수 있습니다. SQLITE3_TEXT 는 주석 등의 특수기호를 제거해버리고 텍스트만 남깁니다.

```php
<-- check_database_secure.php -->
<?php

    $db = new SQLite3('cat_homepage.db');

    $enteredUsername = "babo'--";
    $enteredPassword = "asdf";

    $query = "SELECT * FROM users WHERE username = :username AND password = :password";
    
    $stmt = $db->prepare($query);

    $stmt->bindValue(':username', $enteredUsername, SQLITE3_TEXT);
    $stmt->bindValue(':password', $enteredPassword, SQLITE3_TEXT);

    $result = $stmt->execute();

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

이것을 실행해보면, 주석이 적용되지 않아 SQL injection 으로부터 안전해집니다.

![Untitled](Untitled%20566.png)

그러나, 어떤 특정 쿼리문은 Prepared Statements 로 만드는 것이 어렵습니다.

또한 코드가 복잡해지다보면 기존의 쿼리문과 호환되도록 만들어야해서, 이러한 방식을 적용하는 것이 어려울 수도 있습니다.

따라서 다양한 방법을 통해 SQL injection 을 방어해야합니다.

끝