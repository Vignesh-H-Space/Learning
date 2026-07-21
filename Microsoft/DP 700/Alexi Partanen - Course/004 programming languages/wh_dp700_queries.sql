select *
from dp700_e004.employees;

select *
from dp700_e004.departments;

select *
from dp700_e004.assignments;

select *
from dp700_e004.projects;


select
name
,salary
,concat('$ ',salary) AS salary_string
from dp700_e004.employees
where salary >=75000;

select
e.name
,e.department_id
,d.department_name
from dp700_e004.employees as e
left join dp700_e004.departments as d
on e.department_id = d.department_id
