-- Window Functions and Stored Procedures 
CREATE DATABASE sales_db; 

USE sales_db;

CREATE TABLE sales_data (transaction_id INT PRIMARY KEY, employee_id INT, month VARCHAR(7), sales_amount DECIMAL (10,2));

