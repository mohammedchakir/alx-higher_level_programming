-- This SQL script selects the 'hbtn_0c_0' database and then converts it, the 'first_table', and the 'name' field in 'first_table' to UTF8 (utf8mb4 and utf8mb4_unicode_ci).
USE hbtn_0c_0;
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
