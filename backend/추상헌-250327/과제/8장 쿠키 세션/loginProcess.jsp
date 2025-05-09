<%@ page import="model.LoginDAO, model.LoginDTO" %>
<%@ page import="javax.servlet.http.*, javax.servlet.*" %>
<%@ page contentType="text/html; charset=UTF-8" %>

<%
    // 사용자 입력값 받기
    String id = request.getParameter("id");
    String passwd = request.getParameter("passwd");

    // DAO 호출하여 로그인 확인
    LoginDAO dao = new LoginDAO();
    int result = dao.checkLogin(id, passwd);

    if (result == 1) {
        // 로그인 성공 시 세션에 아이디 저장
        session.setAttribute("id", id);
        response.sendRedirect("loginSuccess.jsp");
    } else if (result == 0) {
        // 비밀번호 불일치
        out.println("비밀번호가 틀렸습니다. <a href='loginForm.jsp'>다시 시도</a>");
    } else {
        // 아이디 없음
        out.println("아이디가 존재하지 않습니다. <a href='loginForm.jsp'>다시 시도</a>");
    }
%>
