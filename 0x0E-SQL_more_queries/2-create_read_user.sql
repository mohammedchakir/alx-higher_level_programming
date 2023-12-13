-- This script creates the database 'hbtn_0d_2' and the user 'user_0d_2'
-- 'user_0d_2' will have only SELECT privilege in the database 'hbtn_0d_2'
-- The password for 'user_0d_2' is set to 'user_0d_2_pwd'
-- The script will not fail if the database 'hbtn_0d_2' or the user 'user_0d_2' already exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
