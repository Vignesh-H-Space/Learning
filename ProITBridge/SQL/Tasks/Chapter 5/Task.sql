-- Creating Database - Library
CREATE DATABASE LibraryDB;


-- Making Library Database for usage
USE LibraryDB;


-- Creating Table Authors
CREATE TABLE Authors (author_id INT PRIMARY KEY, name VARCHAR(100), country VARCHAR(50));

-- Inserting into Table Authors
INSERT INTO Authors VALUES
(1, 'J.K. Rowling', 'UK'),
(2, 'George Orwell', 'UK'),
(3, 'Chetan Bhagat', 'India'),
(4, 'Agatha Christie', 'UK'),
(5, 'Dan Brown', 'USA');

-- Creating Table Books
CREATE TABLE Books (book_id INT PRIMARY KEY, title VARCHAR(100), genre VARCHAR(50), author_id INT, FOREIGN KEY (author_id) REFERENCES Authors(author_id));

-- Inserting into Table Books
INSERT INTO Books VALUES
(101, 'Harry Potter', 'Fantasy', 1),
(102, '1984', 'Dystopian', 2),
(103, 'Half Girlfriend', 'Romance', 3),
(104, 'Murder on the Orient Express', 'Mystery', 4),
(105, 'The Da Vinci Code', 'Thriller', 5);

-- Creating Table Members
CREATE TABLE Members (member_id INT PRIMARY KEY, name VARCHAR(100), join_date DATE);

-- Inserting into Table Members
INSERT INTO Members VALUES
(1, 'Arun', '2024-01-10'),
(2, 'Priya', '2024-02-15'),
(3, 'Rahul', '2024-03-05'),
(4, 'Sneha', '2024-03-20'),
(5, 'Karthik', '2024-04-01');

-- Creating Table Borrow
CREATE TABLE Borrow (borrow_id INT PRIMARY KEY, member_id INT, book_id INT, borrow_date DATE, FOREIGN KEY (member_id) REFERENCES Members(member_id), FOREIGN KEY (book_id) REFERENCES Books(book_id));

-- Inserting into Table Borrow
INSERT INTO Borrow VALUES
(1, 1, 101, '2024-04-10'),
(2, 2, 102, '2024-04-11'),
(3, 3, 103, '2024-04-12'),
(4, 4, 104, '2024-04-13'),
(5, 5, 105, '2024-04-14');

-- INNER JOIN 
-- List all books with their author names 
SELECT Books.title, authors.name from authors 
INNER JOIN Books ON authors.author_id = books.author_id;

-- Show which members borrowed which books (include member name and book title).
SELECT members.name, books.title FROM books
INNER JOIN Borrow ON books.book_id = borrow.book_id
INNER JOIN Members ON borrow.member_id = members.member_id;

-- Display book title, genre, and author country.
SELECT books.title, books.genre , authors.country FROM authors
INNER JOIN books on authors.author_id = books.author_id;