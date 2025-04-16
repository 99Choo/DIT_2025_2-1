<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ page import="java.sql.*"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>레코드 삽입</title>
</head>
<body>

	<%
	Class.forName("org.mariadb.jdbc.Driver");
	try (Connection conn = DriverManager.getConnection("jdbc:mariadb://localhost:3306/choosanghundb", "choosanghun",
			"1111"); Statement stmt = conn.createStatement();) {
		String sql = "INSERT INTO score VALUES (1, '홍길동', 90, 85, 95)," + "                       (2, '성춘향', 88, 92, 80),"
		+ "                       (3, '이몽룡', 75, 70, 78)";
		stmt.executeUpdate(sql);
		out.println("레코드 삽입 성공!");
	} catch (Exception e) {
		out.println("에러 발생: " + e.getMessage());
		e.printStackTrace(new java.io.PrintWriter(out));
	}
	%>

</body>
</html>
