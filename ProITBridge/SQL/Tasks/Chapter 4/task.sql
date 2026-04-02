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
 


----------------      TASK 1 -------------------------
-- Task 1 - Aggregate Functions.
-- 1.Frame 3 problem statements using aggregate functions.
-- 2.Use functions such as COUNT, SUM, AVG, MIN, or MAX.

-- 1. Find the total number of customers 
SELECT COUNT(*) AS TOTAL_CUSTOMERS FROM Customers;

-- 2.Find the average credit limit of all customers
SELECT AVG(creditLimit) AS AVERAGE_CREDIT_LIMIT FROM Customers;