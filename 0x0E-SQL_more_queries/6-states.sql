-- This script creates the database 'hbtn_0d_usa' and the table 'states' in the MySQL server
-- 'states' table structure: id INT unique, auto generated, can’t be null and is a primary key, name VARCHAR(256) can’t be null
-- The script will not fail if the database 'hbtn_0d_usa' or the table 'states' already exists
-- Create database 'hbtn_0d_usa' if it does not exist
-- Create table 'states' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));
