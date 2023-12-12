-- This SQL script updates the score of 'Bob' to 10 in the table 'second_table'.
-- The update is done based on the name field, without using Bob's id value.

UPDATE second_table SET score = 10 WHERE name = 'Bob';
