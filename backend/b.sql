USE backend;

CREATE TABLE MEMBER(
	NAME VARCHAR(30),
	stuID VARCHAR(9),
	addressw VARCHAR(100)
);

INSERT INTO MEMBER(NAME, stuid, addressw) VALUES('홍길동', '123456789', '부산');
INSERT INTO MEMBER(NAME, stuid, addressw) VALUES('홍길서', '123456788', '부산');
INSERT INTO MEMBER(NAME, stuid, addressw) VALUES('홍길남', '123456787', '부산');
INSERT INTO MEMBER(NAME, stuid, addressw) VALUES('홍길북', '123456786', '부산');
INSERT INTO MEMBER(NAME, stuid, addressw) VALUES('홍길동', '123456785', '부산');

CREATE TABLE MEMBER2(
    ID INT PRIMARY key,
    PWD VARCHAR(50),
    NAME VARCHAR(50),
    GENDER CHAR(2),
    PHONE CHAR(13),
    REGDATE DATE
);
COMMIT;

SHOW DATABASES;
