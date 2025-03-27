<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%
    request.setCharacterEncoding("UTF-8"); // 요청 파라미터의 인코딩을 UTF-8로 설정
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body>

 국어: <%=request.getParameter("kor")%><br>
 영어: <%=request.getParameter("eng")%><br>
 수학: <%=request.getParameter("math")%><br>
    
</body>
</html>
