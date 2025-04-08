<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"
    import = "java.sql.*" %>
<%
	request.setCharacterEncoding("utf-8");

 	String name = request.getParameter("name");
	String stuID = request.getParameter("stuID");
	String address = request.getParameter("address");
	
	//1. jdbc 드라이브 로드
	Class.forName("org.mariadb.jdbc.Driver");

	//2. 커넥션 생성
	String url = "jdbc:mariadb://localhost:3306/backend";
	Connection con = DriverManager.getConnection(url, "jskim", "1111");
	
	//3. SQL문 작성(insert)
	String sql = "select * from member where stuID = ?";
	
	//4. SQL문 실행(Statement)		
	PreparedStatement pstmt = con.prepareStatement(sql);
	pstmt.setString(1, stuID);
	
	ResultSet rs = pstmt.executeQuery();	
	
	if(rs.next()){
		String dbAddress = rs.getString("address");
		if(dbAddress.equals(address) ){
			out.println(stuID + "가 로그인 완료했습니다!");
			session.setAttribute("stuID", stuID);
		}else{
			out.println("비번이 달라요!!");
		}
	}else{
		out.println("누구세요??");
	}

%>

<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Insert title here</title>
</head>
<body>
	
</body>
</html>