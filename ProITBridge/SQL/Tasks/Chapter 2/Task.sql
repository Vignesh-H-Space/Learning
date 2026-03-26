-- Creating Database - Sales management 
CREATE DATABASE SalesManagement; 

USE SalesManagement; 

CREATE TABLE ProductLines (ProductLine varchar (30) primary key , textDescription varchar (50), htmlDescription varchar (50), image BLOB ); 

INSERT INTO ProductLines (ProductLine, textDescription, htmlDescription, image) VALUES ('Classic Cars', 'Vintage and classic model cars', NULL, NULL);

INSERT INTO ProductLines (ProductLine, textDescription, htmlDescription, image) VALUES  ('Motorcycles', 'Racing and sports bikes', NULL, NULL);
