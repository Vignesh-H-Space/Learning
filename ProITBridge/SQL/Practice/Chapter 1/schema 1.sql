create database FootballDB;

use FootballDB;

-- Teams table
create table Teams (
    team_id int auto_increment primary key,
    team_name varchar(50),
    city varchar(50),
    coach_name varchar(50)
);

-- Players table
create table Players (
    player_id int auto_increment primary key,
    first_name varchar(50),
    last_name varchar(50),
    position varchar(30),
    birthdate date,
    team_id int,
);