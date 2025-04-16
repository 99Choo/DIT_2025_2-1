<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>테이블 생성</title>
</head>
<body>

<%
    Class.forName("org.mariadb.jdbc.Driver");
    try (
        Connection conn = DriverManager.getConnection(
            "jdbc:mariadb://localhost:3306/choosanghundb", "choosanghun", "1111");
        Statement stmt = conn.createStatement();
    ) {
        // 기존 테이블 있으면 삭제
        stmt.executeUpdate("DROP TABLE IF EXISTS score");

        // 새로 테이블 생성
        String sql = 
            "CREATE TABLE score (" +
            "    num INT PRIMARY KEY," +
            "    name VARCHAR(20)," +
            "    kor INT," +
            "    eng INT," +
            "    math INT" +
            ")";
        stmt.executeUpdate(sql);
        out.println("성적 테이블 생성 성공!");
    } catch(Exception e) {
        out.println("에러 발생: " + e.getMessage());
        e.printStackTrace(new java.io.PrintWriter(out));
    }
%>

</body>
</html>
