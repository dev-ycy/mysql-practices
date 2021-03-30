-- pet table 생성
CREATE TABLE pets (
name varchar(20),
owner varchar(20),
species varchar(20),
gender char(1),
birth date,
death date
);

-- tavle scheme 확인
desc pets;
