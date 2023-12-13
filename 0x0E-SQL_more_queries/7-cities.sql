-- This script creates the database 'hbtn_0d_usa' and the table 'cities' in the MySQL server
-- 'cities' table structure: id INT unique, auto generated, can’t be null and is a primary key, state_id INT references 'states.id', name VARCHAR(256) can’t be null
-- The script will not fail if the database 'hbtn_0d_usa' or the table 'cities' already exists
-- Create database 'hbtn_0d_usa' if it does not exist
-- Create table 'cities' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT AUTO_INCREMENT, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES states(id));
