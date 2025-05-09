<%@ page contentType="text/html; charset=UTF-8" %>
<%
    // 세션 무효화 (로그아웃 처리)
    session.invalidate();
    response.sendRedirect("loginForm.jsp");
%>
