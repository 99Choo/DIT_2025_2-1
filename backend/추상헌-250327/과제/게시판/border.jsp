<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%
	request.setCharacterEncoding("utf-8");
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>작성된 게시글</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { width: 600px; margin: 20px auto; border: 1px solid #ccc; padding: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <%
            // border.html에서 POST 방식으로 전달된 파라미터 받기
            String subject = request.getParameter("subject");
            String writer = request.getParameter("writer");
            String content = request.getParameter("content");
            
            // 값이 없는 경우 폼으로 다시 유도 (이 부분은 선택 사항)
            if(subject == null || writer == null || content == null) {
        %>
                <p>폼 데이터가 누락되었습니다. <a href="border.html">다시 작성하기</a></p>
        <%
            } else {
                // 현재 날짜 및 시간 생성 (작성일)
                String currentDate = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss")
                                     .format(new java.util.Date());
        %>
                <h2>작성된 게시글</h2>
                <p><strong>제목:</strong> <%= subject %></p>
                <p><strong>작성자:</strong> <%= writer %></p>
                <p><strong>작성일:</strong> <%= currentDate %></p>
                <p><strong>내용:</strong></p>
                <!-- 개행 문자(\n)를 <br> 태그로 변환하여 줄바꿈 적용 -->
                <p><%= content.replaceAll("\n", "<br>") %></p>
                <hr>
                <p><a href="border.html">다시 글쓰기</a></p>
        <%
            }
        %>
    </div>
</body>
</html>
