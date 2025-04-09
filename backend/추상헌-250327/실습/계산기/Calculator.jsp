<%@ page contentType="text/html; charset=UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>간단한 계산기</title>
    <style>
        input, button {
            margin: 5px;
            padding: 5px;
        }
    </style>
</head>
<body>
    <h2>간단한 계산기</h2>
    <form method="post">
        <!-- x 입력 필드: 이전에 입력한 값이 있으면 기본 값으로 설정 -->
        x: <input type="number" name="x" value="<%= request.getParameter("x") != null ? request.getParameter("x") : "" %>">
        <br>
        <!-- y 입력 필드 -->
        y: <input type="number" name="y" value="<%= request.getParameter("y") != null ? request.getParameter("y") : "" %>">
        <br>
        <!-- 연산자 버튼들 -->
        <button type="submit" name="op" value="+">+</button>
        <button type="submit" name="op" value="-">-</button>
        <button type="submit" name="op" value="*">*</button>
        <button type="submit" name="op" value="/">/</button>
    </form>

    <hr>

    <% 
        // 폼으로 전달된 파라미터 읽기
        String xStr = request.getParameter("x");
        String yStr = request.getParameter("y");
        String op = request.getParameter("op");

        if (xStr != null && yStr != null && op != null) {
            try {
                int x = Integer.parseInt(xStr);
                int y = Integer.parseInt(yStr);
                String result = "";

                // 선택한 연산자에 따라 계산 수행
                switch (op) {
                    case "+":
                        result = "덧셈 결과는 : " + (x + y);
                        break;
                    case "-":
                        result = "뺄셈 결과는 : " + (x - y);
                        break;
                    case "*":
                        result = "곱셈 결과는 : " + (x * y);
                        break;
                    case "/":
                        if (y == 0) {
                            result = "나눗셈 불능입니다. 0으로 나눌 수 없습니다.";
                        } else {
                            float div = (float)x / y;
                            result = "나눗셈 결과는 : " + div;
                        }
                        break;
                    default:
                        result = "알 수 없는 연산자입니다.";
                }
    %>
                <p><strong><%= result %></strong></p>
    <%
            } catch (NumberFormatException e) {
    %>
                <p>숫자를 정확히 입력하세요.</p>
    <%
            }
        }
    %>
</body>
</html>
