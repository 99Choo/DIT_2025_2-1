<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>로그인 폼</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .container { width: 400px; margin: 0 auto; }
        input { margin: 5px 0; padding: 5px; width: 100%; }
        input[type="submit"] { width: auto; }
    </style>
</head>
<body>
<div class="container">
    <h2>로그인</h2>
    <!-- 로그인 폼: POST 방식으로 loginPro.jsp에 데이터 전송 -->
    <form action="loginPro.jsp" method="post">
        <p>
            <label for="userId">아이디:</label>
            <input type="text" id="userId" name="userId" required>
        </p>
        <p>
            <label for="userPwd">비밀번호:</label>
            <input type="password" id="userPwd" name="userPwd" required>
        </p>
        <p>
            <input type="submit" value="로그인">
        </p>
    </form>
</div>
</body>
</html>
