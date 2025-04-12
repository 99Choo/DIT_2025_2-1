<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>회원 가입 결과</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { width: 600px; margin: 20px auto; }
        table { border-collapse: collapse; width: 100%; }
        table, th, td { border: 1px solid #ccc; }
        th, td { padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
<div class="container">
    <h2>회원 가입 결과</h2>
    <table>
        <tr>
            <th>항목</th>
            <th>입력된 값</th>
        </tr>
        <tr>
            <td>아이디</td>
            <td><%= request.getParameter("userId") %></td>
        </tr>
        <tr>
            <td>비밀번호</td>
            <td><%= request.getParameter("password") %></td>
        </tr>
        <tr>
            <td>이름</td>
            <td><%= request.getParameter("name") %></td>
        </tr>
        <tr>
            <td>이메일</td>
            <td><%= request.getParameter("email") %></td>
        </tr>
        <tr>
            <td>성별</td>
            <td><%= request.getParameter("gender") %></td>
        </tr>
        <tr>
            <td>취미</td>
            <td>
                <%
                    String[] hobbies = request.getParameterValues("hobbies");
                    if (hobbies != null && hobbies.length > 0) {
                        for (int i = 0; i < hobbies.length; i++) {
                            out.print(hobbies[i]);
                            if (i < hobbies.length - 1) out.print(", ");
                        }
                    } else {
                        out.print("선택된 항목이 없습니다.");
                    }
                %>
            </td>
        </tr>
        <tr>
            <td>관심분야</td>
            <td>
                <%
                    String[] interests = request.getParameterValues("interests");
                    if (interests != null && interests.length > 0) {
                        for (int i = 0; i < interests.length; i++) {
                            out.print(interests[i]);
                            if (i < interests.length - 1) out.print(", ");
                        }
                    } else {
                        out.print("선택된 항목이 없습니다.");
                    }
                %>
            </td>
        </tr>
        <tr>
            <td>주소</td>
            <td><%= request.getParameter("address") %></td>
        </tr>
    </table>
    <p><a href="signUp.html">다시 가입하기</a></p>
</div>
</body>
</html>
