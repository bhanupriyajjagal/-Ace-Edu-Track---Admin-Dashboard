CREATE DATABASE college_management;

USE college_management;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_no VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    branch VARCHAR(20) NOT NULL,
    year_of_study INT NOT NULL,
    section VARCHAR(10) NOT NULL
);