-- create DATABASE Test1; 

use studentdb ; 

create table Students (
    studentId int auto_increment primary key ,
    firstname varchar (20),
    lastname varchar (20),
    birthdate date,
    gender varchar (20)
);
