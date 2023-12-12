-- This SQL script displays the top 3 cities by average temperature during July and August, ordered by temperature in descending order.
USE hbtn_0c_0;

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE MONTH=7 OR MONTH=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
