-- SQL script to calculate and display the average temperature by city
-- This script should be executed in the MySQL environment
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
