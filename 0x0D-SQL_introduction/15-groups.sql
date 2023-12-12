-- This SQL script lists the number of records with the same score in the table 'second_table' of the database 'hbtn_0c_0'.
-- The result displays the score and the number of records for each score labeled as 'number'.
-- The list is sorted by the number of records in descending order.
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
