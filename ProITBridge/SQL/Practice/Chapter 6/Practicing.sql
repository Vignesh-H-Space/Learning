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


--------------------- STORED PROCEDURES ---------------

-- Show all Sales 


delimiter $$ 

create procedure get_all_sales()
begin 
    select * from sales_data;
end $$ 

delimiter ; 

call get_all_sales();

-- Employee wise sales 

delimiter $$ 
create procedure get_employee_sales(in emp_id INT)
begin 
    select * from sales_data where employee_id = emp_id ; 
end $$ 

delimiter ; 
call get_employee_sales(103);


-- Get the employee with the highest sales in each month.
SELECT *
FROM (
    SELECT *,
           RANK() OVER (PARTITION BY month ORDER BY sales_amount DESC) AS rnk
    FROM sales_data
) t
WHERE rnk = 1;

-- Find Second Highest Sales per Month
SELECT *
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY month ORDER BY sales_amount DESC) AS rnk
    FROM sales_data
) t
WHERE rnk = 2;

-- Divide employees into performance tiers
SELECT *,
NTILE(3) OVER (ORDER BY sales_amount DESC) AS bucket
FROM sales_data;

-- Top-N filtering (like top 3 sales)
SELECT *,
ROW_NUMBER() OVER (ORDER BY sales_amount DESC) AS row_num
FROM sales_data;

-- Shows cumulative distribution (percentage ranking)
SELECT *,
CUME_DIST() OVER (ORDER BY sales_amount DESC) AS cum_dist
FROM sales_data;

-- Relative rank between 0 and 1
SELECT *,
PERCENT_RANK() OVER (ORDER BY sales_amount DESC) AS percent_rank
FROM sales_data;

--  Procedure with OUT Parameter
DELIMITER $$

CREATE PROCEDURE get_total_sales(OUT total DECIMAL(10,2))
BEGIN
    SELECT SUM(sales_amount) INTO total FROM sales_data;
END $$

DELIMITER ;

CALL get_total_sales(@result);
SELECT @result;


-- Procedure with INOUT Parameter

DELIMITER $$

CREATE PROCEDURE update_bonus(INOUT bonus DECIMAL(10,2))
BEGIN
    SET bonus = bonus + 100;
END $$

DELIMITER ;

SET @b = 500;
CALL update_bonus(@b);
SELECT @b;


-- Loop Procedure

DELIMITER $$

CREATE PROCEDURE count_numbers()
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= 5 DO
        SELECT i;
        SET i = i + 1;
    END WHILE;
END $$

DELIMITER ;


-- Top 2 Sales Per Month
SELECT *
FROM (
    SELECT *,
           DENSE_RANK() OVER (PARTITION BY month ORDER BY sales_amount DESC) AS rnk
    FROM sales_data
) t
WHERE rnk <= 2;

-- Running Average Per Employee
SELECT *,
       AVG(sales_amount) OVER (PARTITION BY employee_id ORDER BY month) AS running_avg
FROM sales_data;

-- Percentage Contribution per Month
SELECT *,
sales_amount * 100.0 /
SUM(sales_amount) OVER (PARTITION BY month) AS percentage_share
FROM sales_data;

-- Window Frame with RANGE
SELECT *,
SUM(sales_amount) OVER (
    ORDER BY sales_amount
    RANGE BETWEEN 100 PRECEDING AND CURRENT ROW
) AS range_sum
FROM sales_data;

--Conditional Window Aggregation
SELECT *,
SUM(CASE WHEN sales_amount > 600 THEN sales_amount ELSE 0 END)
OVER (PARTITION BY month) AS high_sales_sum
FROM sales_data;

-- Procedure with IF Condition
DELIMITER $$

CREATE PROCEDURE check_sales(IN emp_id INT)
BEGIN
    DECLARE total DECIMAL(10,2);

    SELECT SUM(sales_amount) INTO total
    FROM sales_data
    WHERE employee_id = emp_id;

    IF total > 1500 THEN
        SELECT 'High Performer' AS status;
    ELSE
        SELECT 'Needs Improvement' AS status;
    END IF;

END $$

DELIMITER ;

-- Procedure with CASE
DELIMITER $$

CREATE PROCEDURE categorize_sales(IN amount DECIMAL(10,2))
BEGIN
    SELECT 
    CASE
        WHEN amount >= 700 THEN 'Excellent'
        WHEN amount >= 500 THEN 'Good'
        ELSE 'Average'
    END AS category;
END $$

DELIMITER ;

-- Procedure Returning Multiple Results
DELIMITER $$

CREATE PROCEDURE multi_result()
BEGIN
    SELECT * FROM sales_data;
    SELECT SUM(sales_amount) AS total_sales FROM sales_data;
END $$

DELIMITER ;


--- Get the first value in a partition
SELECT *,
FIRST_VALUE(sales_amount) OVER (
    PARTITION BY month 
    ORDER BY sales_amount DESC
) AS highest_in_month
FROM sales_data;

-- Get the last value in a partition
SELECT *,
LAST_VALUE(sales_amount) OVER (
    PARTITION BY month 
    ORDER BY sales_amount
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) AS lowest_in_month
FROM sales_data;

-- Get the “nth” value
SELECT *,
NTH_VALUE(sales_amount, 2) OVER (
    PARTITION BY month 
    ORDER BY sales_amount DESC
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
) AS second_highest
FROM sales_data;