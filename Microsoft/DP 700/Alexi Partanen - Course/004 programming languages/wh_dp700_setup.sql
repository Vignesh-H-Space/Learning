-- Create a schema
CREATE SCHEMA dp700_e004;
GO

-- Create the employees table
CREATE TABLE dp700_e004.employees (
    employee_id INT,
    name VARCHAR(50),
    department_id INT,
    hire_date DATE,
    salary DECIMAL(10, 2)
);
GO
-- Insert data into employees table
INSERT INTO dp700_e004.employees (employee_id, name, department_id, hire_date, salary)
VALUES
    (1, 'John Doe', 101, '2015-06-01', 75000.00),
    (2, 'Jane Smith', 102, '2018-09-15', 85000.00),
    (3, 'Alex Johnson', 103, '2020-01-10', 68000.00),
    (4, 'Sara Lee', 101, '2017-03-12', 72000.00),
    (5, 'Michael Brown', 102, '2019-11-20', 95000.00),
    (6, 'Emma Davis', 103, '2021-07-18', 62000.00);
GO


-- Create the departments table
CREATE TABLE dp700_e004.departments (
    department_id INT,
    department_name VARCHAR(50),
    manager VARCHAR(50),
    location VARCHAR(50)
);
GO

-- Insert data into departments table
INSERT INTO dp700_e004.departments (department_id, department_name, manager, location)
VALUES
    (101, 'Sales', 'Alice Green', 'New York'),
    (102, 'Management', 'Robert White', 'San Francisco'),
    (103, 'IT', 'Sophia Black', 'Seattle'),
    (104, 'Marketing', 'David Blue', 'Chicago');
GO