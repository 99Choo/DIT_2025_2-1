<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="javax.servlet.http.Cookie" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>로그인 결과</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        .container { width: 400px; margin: 0 auto; }
    </style>
</head>
<body>
<div class="container">
<%
    // loginForm.jsp에서 전달된 값 읽어오기
    String userId = request.getParameter("userId");
    String userPwd = request.getParameter("userPwd");

    // 예제: 간단한 로그인 검증 - 아이디가 "admin", 비밀번호가 "1234"이면 로그인 성공으로 가정
    if("admin".equals(userId) && "1234".equals(userPwd)) {
        // 로그인 성공 시 쿠키 생성 및 전송 (쿠키 전송 코드 추가)
        Cookie loginCookie = new Cookie("userId", userId);
        loginCookie.setMaxAge(60 * 60 * 24); // 1일 동안 유효
        response.addCookie(loginCookie);
%>
        <h2>로그인 성공</h2>
        <p>환영합니다, <strong><%= userId %></strong>님!</p>
<%
    } else {
%>
        <h2>로그인 실패</h2>
        <p>아이디 또는 비밀번호가 올바르지 않습니다.</p>
        <p><a href="loginForm.jsp">다시 로그인</a></p>
<%
    }
%>
</div>
</body>
</html>
