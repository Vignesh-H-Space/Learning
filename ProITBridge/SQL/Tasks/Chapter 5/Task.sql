CREATE DATABASE LibraryDB;

USE LibraryDB;

CREATE TABLE Authors (author_id INT PRIMARY KEY, name VARCHAR(100), country VARCHAR(50));

INSERT INTO Authors VALUES
(1, 'J.K. Rowling', 'UK'),
(2, 'George Orwell', 'UK'),
(3, 'Chetan Bhagat', 'India'),
(4, 'Agatha Christie', 'UK'),
(5, 'Dan Brown', 'USA');

