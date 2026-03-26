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
CREATE TABLE Products (ProductCode varchar(30) primary key, ProductName varchar (40) , ProductLine varchar (30) , ProductScale varchar (20) , ProductVendor varchar (30) , ProductDescription varchar (40) , QuantityInStock int, BuyPrice int, MSRP int);
 
-- Inserting into Table Products 
INSERT INTO Products (ProductCode, ProductName, ProductLine, ProductScale, ProductVendor, ProductDescription , QuantityInStock, BuyPrice , MSRP ) VALUES  ('S10_1678', '1969 Harley Davidson', 'Motorcycles', '1:10','Min Lin Diecast','Classic Harley Davidson bike model', 100, 4800, 6500) ;
INSERT INTO Products (ProductCode, ProductName, ProductLine, ProductScale, ProductVendor, ProductDescription , QuantityInStock, BuyPrice , MSRP ) VALUES  ('S12_1099', '1968 Ford Mustang', 'Classic Cars', '1:12','Autoart Studio', 'Classic Ford Mustang model', 50, 9500, 12000);

-- Create Table Order Details
CREATE TABLE orderDetails (orderNumber int primary key, productCode varchar (20), quantityOrdered int, priceEach int, orderLineNumber int );

-- Inserting into Table Order Details
INSERT INTO orderDetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber ) VALUES (30001, 'S10_1678', 2, 6500, 1);
INSERT INTO orderDetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber ) VALUES  (30002, 'S12_1099', 1, 12000, 1);


