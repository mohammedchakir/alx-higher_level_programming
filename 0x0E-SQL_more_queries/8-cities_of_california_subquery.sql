-- This script lists all the cities of California in the database 'hbtn_0d_usa'
-- The results are sorted in ascending order by cities.id
-- The JOIN keyword is not used
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
