-- This script creates the MySQL server user 'user_0d_1' with all privileges
-- The password for 'user_0d_1' is set to 'user_0d_1_pwd'
-- The script will not fail if the user 'user_0d_1' already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
