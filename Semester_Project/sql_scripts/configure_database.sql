CREATE DATABASE IF NOT EXISTS SemesterProject;
CREATE USER IF NOT EXISTS learningdjango@'%' IDENTIFIED BY 'SuperSecure_Password1234';
GRANT ALL ON SemesterProject.* to learningdjango@'%';