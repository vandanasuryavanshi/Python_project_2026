-- create database test123;
-- create database trail123;
-- show databases ;

-- below we cerated a sql database that we will use 
--  create database Practice_sql_2026 ;

-- we will drop data base 
-- drop database test123;
-- drop database trail123;
-- now we will use database 
show databases ;
use  practice_sql_2026;
create table Employee(emp_id int ,emp_name varchar(20) ,city varchar(10) ,dept_id int);
alter table employee
add salary int ;
desc employee ;
insert into Employee values(1001,"shyam",'pune',111,50000);
insert into Employee values (1002,'ram','banglore',111,20000);
insert into Employee values(1003,'priya','mumbai',112,35000);
insert into Employee values(1004,'shivam','nagpur',113,40000);
insert into Employee values(1005,'rishabh','bhopal',113,50000);
insert into employee values(1006,'shekahr','hydrabad',112,35000);
insert into employee values (1007,'riya','indore',111,32000);
insert into employee values(1008,'ridhima','nasik',112,45000);
insert into employee values (1009,'bahadur','jaipur',113,28000);
insert into employee values (1010,'aliza','lakhnow',112,35000);
insert into employee values (1011 ,'govind','delhi',111,40000);
select * from employee;

select count(emp_name) from employee;
-- DDl commands data defination langues create alter rename truncate and drop
-- DQL commands data query langueage select
-- DML data manipulate language insert update and delete
-- DCL data control language grant and revoke 
-- TCL transection control revoke and commit 

create table Department (dept_id int , dept_name varchar(15));
insert into department values (111,"HR"); 
insert into department values (112,"IT");
insert into department values (113,'sales');

select * from department;


select emp.emp_name ,emp.emp_id ,dept.dept_name 
from employee as emp 
left join department as dept 
on emp.dept_id = dept.dept_id;

delete from employee where emp_id =1001
limit 1;

alter table employee 
add primary key(emp_id);


select * from employee 
order by salary desc;

insert into department values 
(114,"finance"),
(115,'marketing');


insert into employee values 
(1012,"sourabh","noida",114,33000),
(1013,'mohit','ayodha',115,29000),
(1014,'suji','hydrabad',114,30000),
(1015,'rehman','firojbad',115,25000);

select *
from employee as emp
left join department as dept 
on dept.dept_id= emp.dept_id
order  by emp.salary ;
alter table department 
add primary key (dept_id);

-- sql constranits not null unique primary key check for any condition


----- update command

update department 
set dept_name="Maketing/ads"
where dept_id=115;

select * from department ;

select  avg(salary) from employee;
select emp_name ,salary from employee
where salary > (select  avg(salary) from employee);


### find the 2nd highest salary from employye
select  max(salary)from employee
where salary < (select max(salary) from employee);



-- ## window function is analyitical function used in sql
select dept_id ,max(salary) from employee 
group by dept_id;


select e.*,
max(salary)  over (partition by  dept_id)  as max_salary
from employee e;


select e.*,
row_number() over() as rn 
from employee e
order by salary desc;

select * from 
(select e.*,
row_number() over() as rn 
from employee e
order by salary desc) x
where x.rn=2;
select e.*,
row_number() over(partition by dept_id order by salary desc ) as rn 
from employee e;

