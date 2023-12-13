-- This script creates the table 'unique_id' in the MySQL server
-- 'unique_id' table structure: id INT with default value 1 and must be unique, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- The script will not fail if the table 'unique_id' already exists
-- Create table 'unique_id' if it does not exist
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1, name VARCHAR(256), UNIQUE (id));
