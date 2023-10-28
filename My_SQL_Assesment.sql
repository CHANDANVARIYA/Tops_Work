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
select *
from workers
where salary = salary;
-- QUE :- (1)6
select*
from workers
limit 6;
-- QUE :- (1)7
select department, count(worker_id)
from workers
group by department
having count(worker_id) >3;
-- QUE :- (1)8
select department, count(worker_id)
from workers
group by department;
-- QUE :- (1)9
SELECT department, last_name, salary
FROM workers as e1
WHERE salary = (select MAX(salary) from workers as e2 where e1.department = e2.department);
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