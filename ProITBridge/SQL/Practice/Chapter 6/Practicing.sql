-- Window Functions and Stored Procedures 
CREATE DATABASE sales_db; 

USE sales_db;

CREATE TABLE sales_data (transaction_id INT PRIMARY KEY, employee_id INT, month VARCHAR(7), sales_amount DECIMAL (10,2));

INSERT INTO sales_data (transaction_id, employee_id, month, sales_amount) VALUES 
(1,101,'2024-01',500.00),
(2,102,'2024-01',600.00),
(3,101,'2024-02',400.00),
(4,103,'2024-02',700.0),
(5,102,'2024-02',650.00),
(6,101,'2024-03',550.00),
(7,103,'2024-03',800.00),
(8,102,'2024-03',700.00),
(9,104,'2024-03',300.00); 

SELECT * FROM sales_data;

-- Write a query that Ranks the sales amount in descending order from the 'sales_data' table and assign a rank to each row 
SELECT * ,
RANK() OVER (ORDER BY sales_amount desc) as RankTable
FROM sales_data;

SELECT * ,
DENSE_RANK() OVER (ORDER BY sales_amount desc) as RankTable
FROM sales_data;


-- Write a query that ranks the sales_amount for each month (partition by month ) in descending order from the sales_data
SELECT * , 
RANK() OVER(partition by month order by sales_amount desc) as  partition_by_month 
FROM sales_data;

-- Write a query that calculates the running total of sales_amount for each employee, order by month from the sales_data
SELECT * , 
SUM(sales_amount) OVER  (PARTITION BY employee_id order by month ) as total
FROM sales_data;

-- Write a query that shows the previous months's sales_amount for each employee from the sales data table, using LAG() function 
SELECT * , 
LAG(sales_amount) OVER  (PARTITION BY employee_id order by month ) as Prev_month
FROM sales_data;

SELECT * , 
LEAD(sales_amount) OVER  (PARTITION BY employee_id order by month ) as Next_month
FROM sales_data;
