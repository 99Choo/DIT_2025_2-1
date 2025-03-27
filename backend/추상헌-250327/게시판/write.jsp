  <%@ page language="java" contentType="text/html; charset=UTF-8"
     	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>게시판 글쓰기</title>
    <style>
        body { font-family: sans-serif; }
        .form-container { width: 400px; margin: 20px auto; border: 1px solid #ccc; padding: 20px; }
        textarea { width: 100%; height: 100px; }
        input[type="text"], input[type="password"] { width: 100%; }
    </style>
</head>
<body>

<div class="form-container">
    <h2>게시판 글쓰기</h2>
    <form method="post" action="write_result.jsp">
        <label>제목: <input type="text" name="title" required></label><br><br>
        <label>작성자: <input type="text" name="name" required></label><br><br>
        <label>내용: <br>
            <textarea name="content" required></textarea>
        </label><br><br>
        <label>비밀번호: <input type="password" name="password" required></label><br><br>
        <button type="submit">작성 완료</button>
    </form>
</div>

</body>
</html>
