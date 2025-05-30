<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>성적 출력</title>
    <style>
        table { width: 600px; text-align: center; border-collapse: collapse; }
        th, td { border: 1px solid #000; padding: 5px; }
        th { background-color: cyan; }
    </style>
</head>
<body>

<table>
    <tr>
        <th>번호</th><th>이름</th>
        <th>국어</th><th>영어</th><th>수학</th>
        <th>총점</th><th>평균</th>
    </tr>

<%
    Class.forName("org.mariadb.jdbc.Driver");
    try (
        Connection conn = DriverManager.getConnection(
            "jdbc:mariadb://localhost:3306/choosanghundb", "choosanghun", "1111");
        Statement stmt = conn.createStatement();
        ResultSet rs = stmt.executeQuery("SELECT * FROM score");
    ) {
        while (rs.next()) {
            int sum = rs.getInt("kor") + rs.getInt("eng") + rs.getInt("math");
%>
    <tr>
        <td><%= rs.getInt("num") %></td>
        <td><%= rs.getString("name") %></td>
        <td><%= rs.getInt("kor") %></td>
        <td><%= rs.getInt("eng") %></td>
        <td><%= rs.getInt("math") %></td>
        <td><%= sum %></td>
        <td><%= String.format("%.2f", (float)sum / 3) %></td>
    </tr>
<%
        }
    } catch(Exception e) {
        e.printStackTrace();
    }
%>

</table>

</body>
</html>
