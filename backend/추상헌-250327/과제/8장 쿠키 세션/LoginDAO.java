package model;

import java.sql.*;

// 데이터베이스에서 회원 인증을 수행하는 DAO 클래스
public class LoginDAO {
    String url = "jdbc:mariadb://localhost:3306/choosanghundb";  // DB URL
    String user = "choosanghun";      // DB 사용자
    String password = "1111";         // DB 비밀번호

    // 로그인 정보 확인 메서드
    public int checkLogin(String id, String passwd) {
        int result = -1;
        String sql = "SELECT passwd FROM member2 WHERE id=?";

        try (
            Connection conn = DriverManager.getConnection(url, user, password);
            PreparedStatement pstmt = conn.prepareStatement(sql);
        ) {
            pstmt.setString(1, id);
            ResultSet rs = pstmt.executeQuery();

            if (rs.next()) {
                // 비밀번호 일치 여부 확인
                if (rs.getString("passwd").equals(passwd)) {
                    result = 1; // 로그인 성공
                } else {
                    result = 0; // 비밀번호 불일치
                }
            } else {
                result = -1; // 아이디 없음
            }
        } catch(Exception e) {
            e.printStackTrace();
        }

        return result;
    }
}
