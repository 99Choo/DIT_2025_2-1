<%@page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>

<%
    //1. DB 연동 드라이버 로드
    Class.forName("org.mariadb.jdbc.Driver");

    //2. 연결 정보 설정
    String url = "jdbc:mariadb://localhost:3306/choosanghundb";
    String user = "choosanghun";
    String pwd = "1111";

    //3. 연결 객체 생성
    Connection con = DriverManager.getConnection(url, user, pwd);

    out.println("연결 성공");

    //4. 연결 객체 해제
    con.close();
%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>DB 연동</title>
</head>
<body>
</body>
</html>
