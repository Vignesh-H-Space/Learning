-- Window Functions and Stored Procedures 

-- Creating Database 

CREATE DATABASE company;

USE DATABASE company;

-- CREATING TABLES 
CREATE TABLE employees(employee_id INT PRIMARY KEY, employee_name VARCHAR(20), department VARCHAR (20));

CREATE TABLE salaries(salary_id INT PRIMARY KEY, employee_id INT, month VARCHAR (10), salary decimal(10,2) , FOREIGN KEY (employee_id) REFERENCES employees(employee_id)) ;

-- INSERTING VALUES INTO TABLE
INSERT INTO employees VALUES
(101, 'Arun', 'IT'),
(102, 'Priya', 'HR'),
(103, 'Karthik', 'Finance'),
(104, 'Sneha', 'IT');
