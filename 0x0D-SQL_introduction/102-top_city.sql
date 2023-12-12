-- This SQL script displays the top 3 cities by average temperature during July and August, ordered by temperature in descending order.
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data -- Replace 'temperature_data' with the actual table name
WHERE MONTH(date_column) IN (7, 8) -- Replace 'date_column' with the actual date column name
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
