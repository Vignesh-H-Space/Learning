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


----------- INNER JOIN  ---------------

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


-- For Join to work properly, adding more data to tables
INSERT INTO Authors VALUES
(6, 'R.K. Narayan', 'India'),
(7, 'J.R.R. Tolkien', 'UK'),
(8, 'Unknown Author', 'Mars');  

INSERT INTO Books VALUES
(106, 'The Hobbit', 'Fantasy', 7),
(107, 'Malgudi Days', 'Fiction', 6),
(108, 'Invisible Book', 'Sci-Fi', NULL);

INSERT INTO Members VALUES
(6, 'Divya', '2024-04-05'),
(7, 'Vikram', '2024-04-06');

SET FOREIGN_KEY_CHECKS = 0;
INSERT INTO Borrow VALUES
(6, 1, 102, '2024-04-15'),
(7, 2, 103, '2024-04-16'),
(8, 3, 999, '2024-04-17'),
(9, 999, 101, '2024-04-18');
SET FOREIGN_KEY_CHECKS = 1;


------------ LEFT JOIN -----------
 
-- List all authors and their books (include authors who haven’t written any books).
SELECT authors.name, books.title FROM authors
LEFT JOIN books ON authors.author_id = books.author_id ; 

-- Show all members and the books they borrowed (include members who haven’t borrowed anything).
SELECT members.name, books.title FROM members
LEFT JOIN borrow ON members.member_id = borrow.member_id
LEFT JOIN books ON borrow.book_id = books.book_id ;

-- List all members with borrow dates (null if no borrow).
SELECT members.name, borrow.borrow_date FROM members
LEFT JOIN borrow ON members.member_id = borrow.member_id; 


------------ RIGHT JOIN ------------

-- List all books and their authors (include books even if author info is missing).
SELECT  books.title, authors.name FROM books
RIGHT JOIN authors ON books.author_id = authors.author_id ; 

-- Show all borrow records and member names (include borrow records even if member missing).
SELECT members.name, books.title
FROM members
RIGHT JOIN borrow ON borrow.member_id = members.member_id
LEFT JOIN books ON borrow.book_id = books.book_id;

-- List all books and matching authors using RIGHT JOIN.
SELECT books.title , authors.name from books
RIGHT JOIN authors ON books.author_id = authors.author_id; 


------------- FULL JOIN ---------------
-- Show all authors and books (include unmatched records from both sides).
SELECT authors.name, books.title FROM authors
LEFT JOIN books ON authors.author_id = books.author_id 
UNION
SELECT authors.name, books.title FROM books
RIGHT JOIN authors ON books.author_id = authors.author_id ; 

-- List all members and borrow records (include members with no borrow and borrow with no member).
SELECT members.name, books.title FROM members
LEFT JOIN borrow ON members.member_id = borrow.member_id
LEFT JOIN books ON borrow.book_id = books.book_id 
UNION
SELECT members.name, books.title FROM members
RIGHT JOIN borrow ON borrow.member_id = members.member_id
LEFT JOIN books ON borrow.book_id = books.book_id;

-- Display all books and borrow entries (include unborrowed books).
SELECT members.name, borrow.borrow_date FROM members
LEFT JOIN borrow ON members.member_id = borrow.member_id
UNION
SELECT members.name, borrow.borrow_date FROM borrow
RIGHT JOIN members ON borrow.member_id = members.member_id ;


------------- CROSS JOIN --------------------
-- Show all possible combinations of members and books.
SELECT members.name , books.title FROM members
CROSS JOIN books;

-- List every author paired with every book.
SELECT authors.name, books.title FROM authors
CROSS JOIN books;

-- Generate all combinations of members and authors.
SELECT members.name , authors.name FROM members
CROSS JOIN authors;


--------------- SELF JOIN ------------------
-- Show pairs of authors from the same country.
SELECT A1.name AS Author1, A2.name AS Author2, A1.country
FROM Authors A1
JOIN Authors A2 
ON A1.country = A2.country ;

-- Find members who joined before other members
SELECT M1.name AS Earlier_Member, M2.name AS Later_Member, M1.join_date, M2.join_date
FROM Members M1
JOIN Members M2
ON M1.join_date < M2.join_date;