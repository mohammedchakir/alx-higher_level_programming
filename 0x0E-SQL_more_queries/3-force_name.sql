-- This script creates the table 'force_name' in the MySQL server
-- 'force_name' table structure: id INT, name VARCHAR(256) which can’t be null
-- The database name will be passed as an argument of the mysql command
-- The script will not fail if the table 'force_name' already exists
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
