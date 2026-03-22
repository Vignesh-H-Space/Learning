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