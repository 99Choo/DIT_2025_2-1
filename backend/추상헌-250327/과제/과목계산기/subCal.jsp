<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>점수 결과</title>
</head>
<body>
    <h2>점수 결과</h2>
    <%
        // 1. 폼에서 전달된 파라미터 값을 문자열로 받음
        String korStr = request.getParameter("kor");
        String engStr = request.getParameter("eng");
        String mathStr = request.getParameter("math");

        // 2. 문자열을 정수로 변환 (숫자 형식이 잘못되었을 경우에 대비하여 예외 처리도 고려할 수 있음)
        int kor = Integer.parseInt(korStr);
        int eng = Integer.parseInt(engStr);
        int math = Integer.parseInt(mathStr);

        // 3. 총점 계산
        int total = kor + eng + math;
        // 4. 평균 계산 (정확한 실수 연산을 위해 하나의 값은 실수로 변환)
        double avg = total / 3.0;
        // 5. 평균은 소수점 3번째 자리에서 반올림되어 소수점 두 자리까지 포맷팅
        String avgFormatted = String.format("%.2f", avg);
    %>
    <p>국어: <%= kor %></p>
    <p>영어: <%= eng %></p>
    <p>수학: <%= math %></p>
    <p>총점: <%= total %></p>
    <p>평균: <%= avgFormatted %></p>
</body>
</html>
