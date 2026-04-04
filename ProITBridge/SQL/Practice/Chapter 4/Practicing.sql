-- Creating Database - Sales management 
CREATE DATABASE SalesManagement; 

-- Making SalesManagement Table for usage
USE SalesManagement; 


-- Create Table Offices 
create table Offices (officeCode varchar(10) primary key, city varchar (30), phone varchar (20), addressLine1 varchar (30), addressLine2 varchar (30), state varchar (15), country varchar (15), postalCode int , territory varchar (10)) ;

-- Inserting into Table Offices 
INSERT Into Offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory ) VALUES ('1', 'Chennai', '+91-44-12345678', 'T Nagar', NULL, 'Tamil Nadu', 'India', '600017', 'APAC') ;
INSERT Into Offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory ) VALUES ('2', 'Bangalore', '+91-80-87654321', 'MG Road', NULL, 'Karnataka', 'India', '560001', 'APAC');


-- Create Table Employees 
create table Employees (employeeNumber int primary key , lastName varchar (20), firstName varchar (20), extension varchar (10), email varchar (40), officeCode varchar (10), reportsTo varchar (30), jobTitle varchar (30), foreign key (officeCode) references Offices (officeCode) );

-- Inserting into Table Employees 
INSERT into Employees (employeeNumber,lastName, firstName , extension ,email, officeCode, reportsTo, jobTitle )  VALUES (1002, 'Kumar', 'Arun', 'x101', 'arun.kumar@classic.com', '1', NULL, 'Sales Manager') ;
INSERT into Employees (employeeNumber,lastName, firstName , extension ,email, officeCode, reportsTo, jobTitle )  VALUES (1056, 'Ravi', 'Suresh', 'x102', 'suresh.ravi@classic.com', '1', 1002, 'Sales Rep') ;
INSERT into Employees (employeeNumber,lastName, firstName , extension ,email, officeCode, reportsTo, jobTitle )  VALUES (1076, 'Sharma', 'Neha', 'x103', 'neha.sharma@classic.com', '2', 1002, 'Sales Rep');


-- Create Table Customers 
Create Table Customers (customerNumber int primary key , customerName varchar (25), contactLastName varchar (25), contactFirstName varchar (25), phone varchar (15), addressLine1 varchar (30), addressLine2 varchar (30), city varchar (15), state varchar (15), postalCode varchar (10), country varchar (15), salesRepEmployeeNumber int, creditLimit Bigint , foreign key  ( salesRepEmployeeNumber) references Employees (employeeNumber) );

-- Inserting into Table Customers
INSERT INTO Customers (customerNumber,customerName,contactLastName, contactFirstName, phone,  addressLine1, addressLine2, city, state , postalCode, country,  salesRepEmployeeNumber, creditLimit) VALUES (2001, 'ABC Traders', 'Rao', 'Vikram', '+91-9876543210','Anna Nagar', NULL, 'Chennai', 'Tamil Nadu', '600040', 'India', 1056, 150000); 
INSERT INTO Customers (customerNumber,customerName,contactLastName, contactFirstName, phone,  addressLine1, addressLine2, city, state , postalCode, country,  salesRepEmployeeNumber, creditLimit) VALUES (2002, 'XYZ Electronics', 'Patel', 'Amit', '+91-9123456789', 'Indiranagar', NULL, 'Bangalore', 'Karnataka', '560038', 'India', 1076, 200000);
 

-- Creating Table ProductLines
CREATE TABLE ProductLines (ProductLine varchar (30) primary key , textDescription varchar (50), htmlDescription varchar (50), image BLOB ); 

-- Inserting into Table ProductLines
INSERT INTO ProductLines (ProductLine, textDescription, htmlDescription, image) VALUES ('Classic Cars', 'Vintage and classic model cars', NULL, NULL);
INSERT INTO ProductLines (ProductLine, textDescription, htmlDescription, image) VALUES  ('Motorcycles', 'Racing and sports bikes', NULL, NULL);


-- Creating Table Products
CREATE TABLE Products (ProductCode varchar(30) primary key, ProductName varchar (40) , ProductLine varchar (30) , ProductScale varchar (20) , ProductVendor varchar (30) , ProductDescription varchar (40) , QuantityInStock int, BuyPrice int, MSRP int , foreign key (productLine) references productLines (productLine)  );
 
-- Inserting into Table Products 
INSERT INTO Products (ProductCode, ProductName, ProductLine, ProductScale, ProductVendor, ProductDescription , QuantityInStock, BuyPrice , MSRP ) VALUES  ('S10_1678', '1969 Harley Davidson', 'Motorcycles', '1:10','Min Lin Diecast','Classic Harley Davidson bike model', 100, 4800, 6500) ;
INSERT INTO Products (ProductCode, ProductName, ProductLine, ProductScale, ProductVendor, ProductDescription , QuantityInStock, BuyPrice , MSRP ) VALUES  ('S12_1099', '1968 Ford Mustang', 'Classic Cars', '1:12','Autoart Studio', 'Classic Ford Mustang model', 50, 9500, 12000);


-- Create Table Orders 
CREATE TABLE orders (orderNumber int, orderDate date , requiredDate date , shippedDate date, status varchar (20), comments varchar (50), customerNumber int );

-- Inserting into Table Orders 
INSERT INTO orders (orderNumber, orderDate, requiredDate , shippedDate , status , comments , customerNumber) VALUES (30001, '2026-01-10', '2026-01-15', '2026-01-13', 'Shipped', 'Delivered on time', 2001);
INSERT INTO orders (orderNumber, orderDate, requiredDate , shippedDate , status , comments , customerNumber) VALUES  (30002, '2026-01-12', '2026-01-18', NULL, 'In Process', NULL, 2002);


-- Create Table Order Details
CREATE TABLE orderDetails (orderNumber int primary key, productCode varchar (20), quantityOrdered int, priceEach int, orderLineNumber int , foreign key (productCode) references Products(productCode) );

-- Inserting into Table Order Details
INSERT INTO orderDetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber ) VALUES (30001, 'S10_1678', 2, 6500, 1);
INSERT INTO orderDetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber ) VALUES  (30002, 'S12_1099', 1, 12000, 1);


-- Create Table Payments 
Create Table Payments (customerNumber int, checkNumber varchar (10),  paymentDate date, amount bigint, foreign key (customerNumber) references Customers (customerNumber));

-- Inserting into Table Payments 
INSERT INTO Payments (customerNumber,checkNumber, paymentDate , amount ) VALUES (2001, 'CHK1001', '2026-01-16', 13000);
INSERT INTO Payments (customerNumber,checkNumber, paymentDate , amount ) VALUES (2002, 'CHK1002', '2026-01-17', 12000);
 
-- DQL and DML Actions -- 

-- Selecting Details of Sales Representatives from Employees Table 
select * from Employees where jobTitle = "Sales Rep";

-- Find all the employees who work in the Chennai Office 
select Employees.firstName, Employees.lastName from Employees 
JOIN Offices on Employees.officeCode = Offices.officeCode
where Offices.city = "Chennai"; 

-- Display customer names and their assigned sales rep names.
select Customers.customerName, Employees.firstname, Employees.lastName from Customers 
JOIN Employees on Employees.employeeNumber = Customers.salesRepEmployeeNumber ;

-- List all products where quantity in stock is less than 80.
select ProductName from Products where QuantityInStock < 80;

-- Get all orders that are not yet shipped.
select orderNumber from Orders where STATUS NOT IN ("Shipped");

-- Show the total payment amount made by each customer.
select Customers.customerName , Payments.amount from Customers
JOIN Payments on Payments.customerNumber = customers.customerNumber ;

-- DML - Insert Data
INSERT into Employees (employeeNumber,lastName, firstName , extension ,email, officeCode, reportsTo, jobTitle )  VALUES (1040, 'Verma', 'Tilak', 'x105', 'tilak.verma@classic.com', '2', 1002, 'Sales Rep');

-- Enabling Updates 
SET SQL_SAFE_UPDATES = 0; 

-- Update all customers in Chennai to increase their credit limit by 10%.
UPDATE Customers
SET creditLimit = creditLimit * 1.10
where city = "Chennai";

-- Delete all orders where status = 'In Process'.
Delete from Orders where status = 'In Process';

-- Update the quantity in stock of product S12_1099 by reducing it by 5.
UPDATE Products
SET QuantityInStock = QuantityInStock - 5 
where productCode = "S12_1099"

-- Insert a new order for customer 2001
INSERT INTO orders (orderNumber, orderDate, requiredDate , shippedDate , status , comments , customerNumber) VALUES  (300015, '2026-03-30', '2026-04-25', NULL, 'In Process', NULL, 2001);



-- Find all customers who have made payments greater than 12000.
SELECT Customers.customerName from Customers
JOIN Payments on Payments.customerNumber = Customers.customerNumber
where Payments.amount > 12000;

-- Find all products that have never been ordered.
SELECT Products.ProductName
FROM Products
LEFT JOIN orderDetails 
ON Products.ProductCode = orderDetails.productCode
WHERE orderDetails.productCode IS NULL;

-- Get the most expensive product (based on MSRP)
SELECT ProductName from Products ORDER BY MSRP DESC LIMIT 1;
-- Other method 
SELECT ProductName from Products WHERE MSRP = (SELECT MAX(MSRP) FROM Products) ;


-- Aggregate Functions -- 

-- Count Function
SELECT COUNT(*) AS Total 
from Products;

-- Sum Function 
SELECT SUM(amount) as Total_Amount
FROM Payments;

-- Average Function
SELECT AVG(BuyPrice) as Average
FROM Products;

-- Min Function 
SELECT MIN(BuyPrice) as Cheapest,
MAX(BuyPrice) as Costliest
FROM Products;

-- Where Function 
SELECT COUNT(*) as ORDER_2026
FROM orders
where YEAR(OrderDate) = 2026; 

SELECT SUM(amount) as SUM_PAID
FROM Payments
where customerNumber = 2002; 


-- Group By Function
SELECT jobTitle, COUNT(*) as TOTAL_COUNT
FROM Employees
GROUP BY jobTitle;

SELECT customerNumber ,SUM(amount) as TOTAL_COST
FROM Payments
GROUP BY customerNumber;

-- Having Function 
SELECT customerNumber ,SUM(amount) as TOTAL_COST
FROM Payments
GROUP BY customerNumber
having TOTAL_COST > 12500;

-- Sub Query Function
SELECT customerNumber, amount from PAYMENTS 
where amount = (SELECT MAX(amount) from Payments);

-- Customers who placed atleast one order 
SELECT customerName from Customers where customerNumber in 
(SELECT customerNumber from orders);

-- Customers with Customer ID who placed atleast one order 
SELECT customerName,customerNumber from Customers where customerNumber in 
(SELECT customerNumber from orders);

-- Get employees who are not assigned to any customer.
SELECT employeeNumber, firstName
FROM Employees
WHERE employeeNumber NOT IN (
    SELECT salesRepEmployeeNumber FROM Customers
);

-- List customers who have never placed an order.
SELECT customerName
FROM Customers
WHERE customerNumber NOT IN (
    SELECT customerNumber FROM Orders
);