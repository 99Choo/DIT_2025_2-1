<%@ page contentType="text/html; charset=UTF-8" %>
<!DOCTYPE html>
<html>
<head>
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
        x: <input type="number" name="x" value="<%= request.getParameter("x") != null ? request.getParameter("x") : "" %>">
        <br>
        y: <input type="number" name="y" value="<%= request.getParameter("y") != null ? request.getParameter("y") : "" %>">
        <br>
        <button type="submit" name="op" value="+">+</button>
        <button type="submit" name="op" value="-">-</button>
        <button type="submit" name="op" value="*">*</button>
        <button type="submit" name="op" value="/">/</button>
    </form>

    <hr>

    <% 
        String xStr = request.getParameter("x");
        String yStr = request.getParameter("y");
        String op = request.getParameter("op");

        if (xStr != null && yStr != null && op != null) {
            try {
                int x = Integer.parseInt(xStr);
                int y = Integer.parseInt(yStr);
                String result = "";

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
