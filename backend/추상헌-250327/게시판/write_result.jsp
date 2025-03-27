<%@ page contentType="text/html; charset=UTF-8" language="java" %>
<%
    request.setCharacterEncoding("UTF-8"); // 한글 깨짐 방지
    String title = request.getParameter("title");
    String name = request.getParameter("name");
    String content = request.getParameter("content");
    String password = request.getParameter("password"); // 출력하지 않음
%>

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>게시글 확인</title>
    <style>
        body { font-family: sans-serif; }
        .result-container { width: 400px; margin: 20px auto; border: 1px solid #ccc; padding: 20px; }
    </style>
</head>
<body>

<div class="result-container">
    <h2>입력된 게시글 정보</h2>
    <p><strong>제목:</strong> <%= title %></p>
    <p><strong>작성자:</strong> <%= name %></p>
    <p><strong>내용:</strong><br><pre><%= content %></pre></p>
    <p><strong>※ 비밀번호는 보안을 위해 저장됩니다. (화면에 표시되지 않음)</strong></p>
</div>

</body>
</html>
