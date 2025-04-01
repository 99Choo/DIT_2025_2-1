SHOW DATABASES;
SELECT NOW();
SELECT * FROM mysql.USER;
-- 데이터베이스 생성
Create database backend; 
-- 사용자 생성
Create user choo@localhost identified BY '1111';
-- 사용자 생성 확인
SELECT * FROM mysql.user;
-- 사용자에게 권한 부여 
grant all privileges on backend.* to choo@localhost with grant OPTION; 
-- 사용자에게 모든 권한 부여 / -- 다른 사람에게 권한을 부여할 수 있는 권한도 부여.
DROP USER 'ID'@'Host';