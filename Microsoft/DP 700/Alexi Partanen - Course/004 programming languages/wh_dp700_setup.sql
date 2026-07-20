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
