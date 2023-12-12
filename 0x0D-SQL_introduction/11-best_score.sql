-- This SQL script lists all records with a score >= 10 in the table 'second_table' of the database 'hbtn_0c_0'.
-- The results display both the score and the name, in that order.
-- Records are ordered by score, from highest to lowest.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
