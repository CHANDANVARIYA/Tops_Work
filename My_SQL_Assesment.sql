-- QUE :-(1)1
select *
from workers
order by First_name; 
select *
from workers
order by Department desc;
-- QUE :-(1)2
select *
from workers
where (first_name = "vipul") or (First_name = "Satish");
-- QUE :-(1)3
select *
from workers
where first_name like "_____h";
-- QUE :- (1)4
select *
from workers
where salary between 50000 and 100000; 
-- QUE :- (1)5
select salary, Department
from workers
group by salary, department
having count(*) >  1;
-- QUE :- (1)6
select*
from workers
limit 6;
-- QUE :- (1)7
select department, count(*) as "CountOf_Emp"
from workers
group by department
having count(*) <3;
-- QUE :- (1)8
select department, count(*)
from workers
group by department;
-- QUE :- (1)9
SELECT department, last_name, salary
FROM workers as e1
WHERE salary = (select MAX(salary) from workers as e2 where e1.department = e2.department);

select department, last_name,salary
from workers
where (Department,salary) in (select Department, max(salary) from workers group by Department);
-- QUE :- (2)1
select *
from student;
-- QUE :- (2)2
select StdName, DOB 
from student;
-- QUE :- (2)3
select * 
from student 
where percentage >= 80; 
-- QUE :- (2)4
select STD_NAME, steam, Percentage 
from student
where percentage > 80; 
-- QUE :- (2)5
select * 
from student 
where steam = 'Science' and percentage > 75;