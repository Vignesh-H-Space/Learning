-- Creating Database - Sales management 
CREATE DATABASE SalesManagement; 

-- Making SalesManagement Table for usage
USE SalesManagement; 


-- Creating Table Productions
CREATE TABLE ProductLines (ProductLine varchar (30) primary key , textDescription varchar (50), htmlDescription varchar (50), image BLOB ); 

-- Inserting into Table Productions
INSERT INTO ProductLines (ProductLine, textDescription, htmlDescription, image) VALUES ('Classic Cars', 'Vintage and classic model cars', NULL, NULL);
INSERT INTO ProductLines (ProductLine, textDescription, htmlDescription, image) VALUES  ('Motorcycles', 'Racing and sports bikes', NULL, NULL);


-- Creating Table Products
CREATE TABLE Products (ProductCode varchar(30) primary key, ProductName varchar (40) , ProductLine varchar (30) , ProductScale varchar (20) , ProductVendor varchar (30) , ProductDescription varchar (40) , QuantityInStock int, BuyPrice int, MSRP int , foreign key (productLine) references productLines (productLine)  );
 
-- Inserting into Table Products 
INSERT INTO Products (ProductCode, ProductName, ProductLine, ProductScale, ProductVendor, ProductDescription , QuantityInStock, BuyPrice , MSRP ) VALUES  ('S10_1678', '1969 Harley Davidson', 'Motorcycles', '1:10','Min Lin Diecast','Classic Harley Davidson bike model', 100, 4800, 6500) ;
INSERT INTO Products (ProductCode, ProductName, ProductLine, ProductScale, ProductVendor, ProductDescription , QuantityInStock, BuyPrice , MSRP ) VALUES  ('S12_1099', '1968 Ford Mustang', 'Classic Cars', '1:12','Autoart Studio', 'Classic Ford Mustang model', 50, 9500, 12000);


-- Create Table Order Details
CREATE TABLE orderDetails (orderNumber int primary key, productCode varchar (20), quantityOrdered int, priceEach int, orderLineNumber int , foreign key (productCode) references Products(productCode) );

-- Inserting into Table Order Details
INSERT INTO orderDetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber ) VALUES (30001, 'S10_1678', 2, 6500, 1);
INSERT INTO orderDetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber ) VALUES  (30002, 'S12_1099', 1, 12000, 1);


-- Create Table Orders 
CREATE TABLE orders (orderNumber int, orderDate date , requiredDate date , shippedDate date, status varchar (20), comments varchar (50), customerNumber int , foreign key (orderNumber) references orderDetails(orderNumber) );

-- Inserting into Table Orders 
INSERT INTO orders (orderNumber, orderDate, requiredDate , shippedDate , status , comments , customerNumber) VALUES (30001, '2026-01-10', '2026-01-15', '2026-01-13', 'Shipped', 'Delivered on time', 2001);
INSERT INTO orders (orderNumber, orderDate, requiredDate , shippedDate , status , comments , customerNumber) VALUES  (30002, '2026-01-12', '2026-01-18', NULL, 'In Process', NULL, 2002);


-- Create Table Customers 
Create Table Customers (customerNumber int primary key , customerName varchar (25), contactLastName varchar (25), contactFirstName varchar (25), phone varchar (15), addressLine1 varchar (30), addressLine2 varchar (30), city varchar (15), state varchar (15), postalCode varchar (10), country varchar (15), salesRepEmployeeNumber int, creditLimit Bigint );

