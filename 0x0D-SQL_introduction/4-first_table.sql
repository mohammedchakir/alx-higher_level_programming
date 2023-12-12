-- This SQL script creates a table called 'first_table' in the current database.
-- The table has an 'id' column of type INT and a 'name' column of type VARCHAR(256).
-- If the table already exists, the script does not fail.

CREATE TABLE IF NOT EXISTS first_table (id INT,name VARCHAR(256));
