CREATE DATABASE LibraryDB;

USE LibraryDB;

CREATE TABLE Authors (author_id INT PRIMARY KEY, name VARCHAR(100), country VARCHAR(50));

INSERT INTO Authors VALUES
(1, 'J.K. Rowling', 'UK'),
(2, 'George Orwell', 'UK'),
(3, 'Chetan Bhagat', 'India'),
(4, 'Agatha Christie', 'UK'),
(5, 'Dan Brown', 'USA');

CREATE TABLE Books (book_id INT PRIMARY KEY, title VARCHAR(100), genre VARCHAR(50), author_id INT, FOREIGN KEY (author_id) REFERENCES Authors(author_id));

INSERT INTO Books VALUES
(101, 'Harry Potter', 'Fantasy', 1),
(102, '1984', 'Dystopian', 2),
(103, 'Half Girlfriend', 'Romance', 3),
(104, 'Murder on the Orient Express', 'Mystery', 4),
(105, 'The Da Vinci Code', 'Thriller', 5);


CREATE TABLE Members (member_id INT PRIMARY KEY, name VARCHAR(100), join_date DATE);

INSERT INTO Members VALUES
(1, 'Arun', '2024-01-10'),
(2, 'Priya', '2024-02-15'),
(3, 'Rahul', '2024-03-05'),
(4, 'Sneha', '2024-03-20'),
(5, 'Karthik', '2024-04-01');