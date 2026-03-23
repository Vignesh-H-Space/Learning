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
    foreign key (team_id) references Teams(team_id)
);

-- Matches table
create table Matches (
    match_id int auto_increment primary key,
    home_team_id int,
    away_team_id int,
    match_date date,
    stadium varchar(50),
    home_score int,
    away_score int,
    foreign key (home_team_id) references Teams(team_id),
    foreign key (away_team_id) references Teams(team_id)
);


-- Goals table (who scored in which match)
create table Goals (
    goal_id int auto_increment primary key,
    match_id int,
    player_id int,
    goal_time int, -- minute of goal
    foreign key (match_id) references Matches(match_id),
    foreign key (player_id) references Players(player_id)
);

-- Player Statistics table
create table PlayerStats (
    stat_id int auto_increment primary key,
    player_id int,
    matches_played int,
    goals_scored int,
    assists int,
    yellow_cards int,
    red_cards int,
    foreign key (player_id) references Players(player_id)
);

create table Seasons (
    season_id int auto_increment primary key,
    season_name varchar(20), -- e.g. 2024/25
    start_date date,
    end_date date
);

create table Transfers (
    transfer_id int auto_increment primary key,
    player_id int,
    from_team_id int,
    to_team_id int,
    transfer_date date,
    transfer_fee decimal(10,2),
    foreign key (player_id) references Players(player_id)
);


INSERT INTO Seasons (season_name, start_date, end_date) VALUES
('2024/25', '2024-08-01', '2025-05-31'),
('2025/26', '2025-08-01', '2026-05-31');

INSERT INTO Teams (team_name, city, coach_name) VALUES
('Chennai Strikers', 'Chennai', 'Ravi Kumar'),
('Madurai Warriors', 'Madurai', 'Arjun Singh'),
('Coimbatore Kings', 'Coimbatore', 'David Raj'),
('Trichy Titans', 'Trichy', 'Suresh Babu');

