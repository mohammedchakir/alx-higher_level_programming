-- This script creates the table 'id_not_null' in the MySQL server
-- 'id_not_null' table structure: id INT with default value 1, name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- The script will not fail if the table 'id_not_null' already exists
-- Create table 'id_not_null' if it does not exist
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
