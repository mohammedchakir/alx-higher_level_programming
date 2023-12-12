-- This SQL script calculates and displays the average temperature by city, ordered by temperature in descending order.
SELECT city, AVG(temperature) AS avg_temp
FROM temperature_data -- Replace 'temperature_data' with the actual table name
GROUP BY city
ORDER BY avg_temp DESC;
