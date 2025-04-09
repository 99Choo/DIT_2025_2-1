<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	//쿠키 생성
	Cookie c =  new Cookie("id", "gildong");
	c.setMaxAge(60);
	response.addCookie(c);
%>

<a href="useCookie.jsp">여기를 눌러주세요</a>