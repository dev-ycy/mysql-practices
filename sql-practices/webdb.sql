-- drop database employee;
-- drop user 'employee'@'localhost';

-- create database employees;
-- create user 'employees'@'localhost' identified by 'employees';
-- grant all privileges on employees.* to 'employees'@'localhost';
-- flush privileges;

-- -- mysql -u employee -D employee -p < employee.sql
-- -- cmd 에서는 가능한데 여기에선 안됨 

-- 위에꺼 무시 -------------------------------------------------
desc emaillist;

-- insert
-- insert into emaillist values(null, '안', '대혁', 'kickscar@gmail.com'); 
-- insert into emaillist values(null, '둘', '리', 'dooly@gmail.com'); 

-- select
select no, first_name, last_name, email from emaillist order by no desc;



