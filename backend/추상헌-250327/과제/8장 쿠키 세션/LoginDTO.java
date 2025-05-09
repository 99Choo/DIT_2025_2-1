package model;

// 사용자 정보를 담는 DTO 클래스
public class LoginDTO {
    private String id;        // 사용자 아이디
    private String passwd;    // 사용자 비밀번호

    // Getter, Setter
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getPasswd() {
        return passwd;
    }

    public void setPasswd(String passwd) {
        this.passwd = passwd;
    }
}
