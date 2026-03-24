-- create DATABASE Test1; 

use studentdb ; 

create table Students (
    studentId int auto_increment primary key ,
    firstname varchar (20),
    lastname varchar (20),
    birthdate date,
    gender varchar (20)
);

create table Courses (
    courseid int auto_increment primary key, 
    coursename varchar (50),
    credits int 
);

create table Enrollment (
    enrollmentid int auto_increment primary key, 
    coursename varchar (50),
    studentid int,
    courseid int ,
    enrollmentdate date ,
    foreign key (studentid) references Students(studentid),
    foreign key (courseid) references Courses(courseid)
);

Insert into students (firstname, lastname, birthdate, gender)
values ("John", "Doe", "2002-05-13","Male"); 

Insert into students (firstname, lastname, birthdate, gender)
values ("John", "Doe", "2002-05-13","Male"),
("July", "Mary", "2004-01-24","Female"),
("Angelo", "Mathew", "2006-03-06","Male"),
("Sunder", "Raj", "2001-06-23","Male"); 

Insert into courses (coursename, credits)
values ("Mathematics",23),
("Social",43),
("Science",63),
("English",13);

Insert into courses (coursename, credits)
values ("Second Language",55);

Insert into enrollment (studentid, courseid, enrollmentdate)
values (1,1,"2025-12-13"),
(1,2,"2023-04-16"),
(2,1,"2025-02-25"),
(2,4,"2025-06-28");

select * from students;
