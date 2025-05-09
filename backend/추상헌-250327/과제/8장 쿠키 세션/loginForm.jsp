<%@ page contentType="text/html; charset=UTF-8" %>
<!DOCTYPE html>
<html>
<head><title>로그인</title></head>
<body>
    <h2>로그인</h2>
    <!-- 로그인 폼: POST 방식으로 loginProcess.jsp에 전송 -->
    <form method="post" action="loginProcess.jsp">
        아이디: <input type="text" name="id"><br>
        비밀번호: <input type="password" name="passwd"><br>
        <input type="submit" value="로그인">
    </form>
</body>
</html>
