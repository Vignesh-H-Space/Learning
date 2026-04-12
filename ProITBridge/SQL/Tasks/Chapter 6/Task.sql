-- Window Functions and Stored Procedures 

-- Creating Database 

CREATE DATABASE company;

USE company;

-- CREATING TABLES 
CREATE TABLE employees(employee_id INT PRIMARY KEY, employee_name VARCHAR(20), department VARCHAR (20));

CREATE TABLE salaries(salary_id INT PRIMARY KEY, employee_id INT, month VARCHAR (10), salary decimal(10,2) , FOREIGN KEY (employee_id) REFERENCES employees(employee_id)) ;

-- INSERTING VALUES INTO TABLE
INSERT INTO employees VALUES
(101, 'Arun', 'IT'),
(102, 'Priya', 'HR'),
(103, 'Karthik', 'Finance'),
(104, 'Sneha', 'IT');

INSERT INTO salaries VALUES
(1,101,'2024-01',50000),
(2,102,'2024-01',40000),
(3,103,'2024-01',60000),
(4,101,'2024-02',55000),
(5,102,'2024-02',42000),
(6,103,'2024-02',62000),
(7,104,'2024-02',45000),
(8,101,'2024-03',58000),
(9,102,'2024-03',43000),
(10,103,'2024-03',65000),
(11,104,'2024-03',47000);


-- Rank all employees based on their salary in descending order.
SELECT * ,
RANK() OVER (ORDER BY salary desc) as SALARY_ORDER
FROM salaries; 

-- Rank employees within each department based on salary (highest first).
SELECT employees.employee_id, salaries.month, salaries.salary, employees.employee_name, employees.department,
DENSE_RANK() OVER (PARTITION BY department ORDER BY salary desc) as SALARY_ORDER
FROM salaries
JOIN employees ON salaries.employee_id = employees.employee_id ; 

-- Calculate the running total salary for each employee over months.
SELECT * ,
SUM(salary) OVER (PARTITION BY employee_id ORDER BY month ) as TOTAL_SALARY
FROM salaries;

-- Show each employee’s salary along with the average salary of their department.
SELECT *,
AVG(salary) OVER (PARTITION BY department ORDER BY salary) as AVG_Salary
FROM salaries
JOIN employees ON salaries.employee_id = employees.employee_id ;

