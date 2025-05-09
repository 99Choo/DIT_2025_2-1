<%@ page contentType="text/html; charset=UTF-8" %>
<%
    // 세션에서 아이디 가져오기
    String id = (String) session.getAttribute("id");

    // 세션 정보 없으면 로그인 폼으로 이동
    if (id == null) {
        response.sendRedirect("loginForm.jsp");
        return;
    }
%>
<!-- 로그인 성공 화면 -->
<h2><%= id %>님, 로그인 성공!</h2>
<a href="logout.jsp">로그아웃</a>
